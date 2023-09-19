import boto3
import os

# S3クライアントを作成
s3 = boto3.client('s3')

# バケット名とオブジェクトキー、ファイル名を指定
bucket_name = os.getenv('MY_BUCKET_NAME')
object_key = 'sample_upload.txt'

download_folder = 's3_txt'
download_file = os.path.join(
    download_folder, 
    's3_simple.txt'
    )

# ファイルのダウンロード
s3.download_file(bucket_name, object_key, download_file)

print("Done")