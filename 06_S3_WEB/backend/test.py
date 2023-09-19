import requests
import json

# 各種設定
URL = f"http://127.0.0.1"
PRESIGNED_URL = f"http://127.0.0.1/presigned"
QUERY_DATA = {
    'object_key': "sample.txt",
    "request_type": "get_object"
    }
DOWNLOAD_FILE = "sample.txt"

def main():
    
    # S3Get (http://127.0.0.1)
    response = requests.get(URL)
    print(f"\nurl: {response.url}")
    print(f"status code: {response.status_code}")
    print(f"content: {json.loads(response.json())}")

    # S3Presigned (http://127.0.0.1/presigned)
    response = requests.get(PRESIGNED_URL, params=QUERY_DATA)
    print(f"\nurl: {response.url}")
    print(f"status code: {response.status_code}")

    # ダウンロード
    response_presigned_url = json.loads(response.json())["presigned_url"]
    response = requests.get(response_presigned_url)
    if response.status_code == 200:
        # ダウンロードが成功した場合
        with open(DOWNLOAD_FILE, 'wb') as f:
            f.write(response.content)
    else:
        # ダウンロードが失敗した場合
        print(f"ダウンロードに失敗しました。HTTPステータスコード: {response.status_code}")

if __name__ == '__main__':
    main()