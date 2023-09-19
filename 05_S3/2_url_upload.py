import boto3
import requests
import os

# S3クライアントを作成
s3 = boto3.client('s3')

# バケット名とオブジェクトキー、ファイル名を指定
bucket_name = os.getenv('MY_BUCKET_NAME')
object_key = 'sample_url_upload.txt'
upload_file = 's3_txt/sample.txt'

# Presigned URLの生成
presigned_url = s3.generate_presigned_url(
    'put_object',
    Params={'Bucket': bucket_name, 'Key': object_key},
    ExpiresIn=60  # 有効期限（秒単位）を設定
)

# Presigned URLでデータ取得
with open(upload_file, 'rb') as file:
    text_data = file.read()
response = requests.put(presigned_url, data=text_data)

print("Done")
