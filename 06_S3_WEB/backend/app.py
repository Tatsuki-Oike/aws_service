from flask import Flask, request, render_template
from flask_restful import Resource, Api
from flask_cors import CORS
import json
import boto3
from botocore.config import Config
import os

# APIの準備
app = Flask(__name__,
    static_folder="../frontend/dist/static",
    template_folder="../frontend/dist")
api = Api(app)
CORS(app)

# S3バケットの情報
s3 = boto3.client(
    's3', 
    region_name='ap-northeast-1',
    config=Config(signature_version="s3v4")
    )
bucket_name = os.getenv('MY_BUCKET_NAME')

# バケット内のオブジェクト受け取る
class S3Get(Resource):
    def get(self):
        try:

            # バケット内のオブジェクト一覧を取得
            file_list = []
            response = s3.list_objects(Bucket=bucket_name)

            # オブジェクト一覧を取得
            if 'Contents' in response:
                for obj in response['Contents']:
                    file_list.append(obj['Key'])
            else:
                file_list = ["no contents"]

            response = {"file_list": file_list}
        except Exception as e:
            response = {"error": str(e)}
        return json.dumps(response)

# Presigned URLの取得
class S3Presigned(Resource):
    def get(self):
        try:
            # クエリデータ受け取り
            query_data = request.args
            object_key = query_data["object_key"]
            request_type = query_data["request_type"]

            # Presigned URLの生成
            presigned_url = s3.generate_presigned_url(
                str(request_type),
                Params={'Bucket': bucket_name, 'Key': object_key},
                ExpiresIn=600  # 有効期限（秒単位）を設定
            )

            response = {
                "bucket_name": bucket_name,
                "object_key": object_key,
                "presigned_url": str(presigned_url)
                }
        except Exception as e:
            response = {"error": str(e)}
        return json.dumps(response)

# ルーティング
api.add_resource(S3Get, '/api')
api.add_resource(S3Presigned, '/api/presigned')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')

# サーバー起動
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=80)