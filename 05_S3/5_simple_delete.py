import boto3
import os

# S3クライアントを作成
s3 = boto3.client('s3')

# バケット名とオブジェクトキーを指定
bucket_name = os.getenv('MY_BUCKET_NAME')
object_key = 'sample_upload.txt'

# オブジェクトの削除
s3.delete_object(Bucket=bucket_name, Key=object_key)

print("Done")
