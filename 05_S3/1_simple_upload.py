import boto3
import os

# S3クライアントを作成
s3 = boto3.client('s3')

# バケット名とオブジェクトキー、アップロードするファイル名を指定
bucket_name = os.getenv('MY_BUCKET_NAME')
object_key = 'sample_upload.txt'
upload_file = 's3_txt/sample.txt'

# ファイルのアップロード
s3.upload_file(upload_file, bucket_name, object_key)

print("Done")