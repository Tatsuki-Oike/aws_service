# 0 AWS

* S3作成
* Cross-Origin Resource Sharing (CORS)
* IAMロール作成
* EC2作成
  * セキュリティグループ (22, 80, 5000)

<br>
Cross-Origin Resource Sharing (CORS)

```js
[
    {
        "AllowedHeaders": [
            "*"
        ],
        "AllowedMethods": [
            "GET",
            "PUT",
            "DELETE"
        ],
        "AllowedOrigins": [
            "*"
        ],
        "ExposeHeaders": [],
        "MaxAgeSeconds": 3000
    }
]
```

<br>

# 1 ローカルでフロントエンド開発

```sh
npm install -g @vue/cli
```

```sh
cd ./aws_service/06_S3_WEB # 現在のディレクトリ移動
npm init vite-app frontend # プロジェクト(フォルダ)作成
cd frontend # 現在のディレクトリ移動
npm install
npm install axios
npm install vue-router
npm install vuex
npm run dev # サーバー立てる
```

```sh
npm run build # buildファイルを作成する
```

<br>

# 2 Frontend

## 2.1 ソースコード

```sh
sudo yum install -y git
git --version
git clone ~~
cd ./aws_service/06_S3_WEB/frontend
```

## 2.2 WEBサーバー

```sh
sudo yum install httpd -y # Apache Install
sudo systemctl start httpd # Apache 起動
sudo cp -r dist/* /var/www/html # WEBアプリフォルダ移動
```

# 3 Backend

```sh
export MY_BUCKET_NAME='bucket-name'
```

```sh
cd ../backend
python3 -m venv venv # 仮想環境作成
source venv/bin/activate # 環境の中にはいる
python3 -m pip install --upgrade pip # pip upgrade
pip3 install -r requirements.txt # ライブラリインストール
sudo venv/bin/python app.py
python3 test.py
```

<br>