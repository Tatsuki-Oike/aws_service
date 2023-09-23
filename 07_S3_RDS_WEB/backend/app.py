import uuid
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
from flask_cors import CORS
import json
import boto3
from botocore.config import Config
import os

import config

# 接続情報
USER = config.USER
PASSWORD = config.PASSWORD
HOST = config.HOST
DATABASE = config.DATABASE

# DB, API準備
db = SQLAlchemy()
app = Flask(__name__,
    static_folder="../frontend/dist/static",
    template_folder="../frontend/dist")
app.config["SQLALCHEMY_DATABASE_URI"] = f'mysql+pymysql://{USER}:{PASSWORD}@{HOST}/{DATABASE}'
db.init_app(app)
api = Api(app)
CORS(app)

# S3バケットの情報
s3 = boto3.client(
    's3',  
    region_name='ap-northeast-1',
    endpoint_url='https://s3-ap-northeast-1.amazonaws.com',
    config=Config(signature_version="s3v4"),
    )
bucket_name = os.getenv('MY_BUCKET_NAME')

# テーブル作成
class ImageContent(db.Model):
    __tablename__ = "imageContent"
    image_id = db.Column(db.String(50), primary_key=True)
    image_name = db.Column(db.String(30), unique=True, nullable=False)
    image_url = db.Column(db.String(80), unique=True, nullable=False)

class S3RDS(Resource):

    # RDSのテーブルの中身取得
    def get(self):
        try:
            # テーブルの中身を取得
            images = db.session.query(ImageContent).all()
            image_list = []

            for image in images:
                image_list.append(
                    {
                        "image_id": str(image.image_id),
                        "image_name": str(image.image_name),
                        "image_url": str(image.image_url)
                    }
                )

            response = {"image_list": image_list}
        except Exception as e:
            response = {"error": str(e)}
        return json.dumps(response)
    
    def put(self):
        try:
            # JSONデータ受け取り
            json_data = json.loads(request.data)
            image_name = json_data["image_name"]

            # Presigned URLの生成
            presigned_url = s3.generate_presigned_url(
                "put_object",
                Params={'Bucket': bucket_name, 'Key': image_name},
                ExpiresIn=600  # 有効期限（秒単位）を設定
            )

            # テーブルに項目追加 or 書き換え
            image_url = f'https://{bucket_name}.s3.amazonaws.com/{image_name}'
            image = ImageContent(
                image_id = uuid.uuid4(),
                image_name = image_name,
                image_url = image_url
                )
            db.session.add(image)
            db.session.commit()

            # response
            response = {
                "presigned_url": str(presigned_url)
                }
        except Exception as e:
            response = {"error": str(e)}
        return json.dumps(response)
    
    def delete(self):
        try:
            # クエリデータ受け取り
            query_data = request.args
            image_id = query_data["image_id"]

            # S3のデータ消去
            image = db.session.query(ImageContent).filter_by(image_id=str(image_id)).first()
            object_key = image.image_name
            s3.delete_object(Bucket=bucket_name, Key=object_key)
            
            # テーブルの中身を消去
            db.session.query(ImageContent).filter_by(image_id=str(image_id)).delete()
            db.session.commit()

            response = {"status": "SUCCESS"}
        except Exception as e:
            response = {"error": str(e)}
        return json.dumps(response)

api.add_resource(S3RDS, '/')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')

if __name__ == '__main__':

    # テーブル作成
    with app.app_context():
        db.create_all()

    # サーバー起動
    app.run(debug=True, host="0.0.0.0", port=80)