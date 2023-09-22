import boto3
import requests
import os

# S3クライアントを作成
s3 = boto3.client('s3')

# バケット名とオブジェクトキー、ファイル名を指定
bucket_name = os.getenv('MY_BUCKET_NAME')
object_key = 'sample_url_upload.txt'

download_folder = 's3_txt'
download_file = os.path.join(
    download_folder, 
    's3_presigned_url.txt'
    )

# Presigned URLの生成
presigned_url = s3.generate_presigned_url(
    'get_object',
    Params={'Bucket': bucket_name, 'Key': object_key},
    ExpiresIn=60  # 有効期限（秒単位）を設定
)

# Presigned URLでデータ取得
response = requests.get(presigned_url)

if response.status_code == 200:
    # ダウンロードが成功した場合
    with open(download_file, 'wb') as f:
        f.write(response.content)
    print("Done")
else:
    # ダウンロードが失敗した場合
    print(f"ERROR: {response.status_code}")
