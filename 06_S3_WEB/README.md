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
cd ./aws_service/06_S3_WEB
npm init vite-app frontend
cd frontend
npm install
npm install axios
npm install vue-router
npm install vuex
npm run dev
```

<br>

# 2 Frontend

## 2.1 ソースコード

```sh
sudo yum install -y git
git --version
git clone https://github.com/Tatsuki-Oike/aws_service.git
cd ./aws_service/06_S3_WEB/frontend
```

## 2.2 build

```sh
npm install
npm install axios
npm install vue-router
npm install vuex
npm run build
```

## 2.3 WEBサーバー

```sh
sudo yum install httpd -y
sudo systemctl start httpd
sudo cp -r dist/* /var/www/html
```

# 3 Backend

```sh
export MY_BUCKET_NAME='bucket-name'
```

```sh
cd ../backend
python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
pip3 install -r requirements.txt
sudo venv/bin/python app.py
```

<br>