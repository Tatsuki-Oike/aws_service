# 0 AWS

* S3作成
* Cross-Origin Resource Sharing (CORS)
* IAMロール作成
* EC2作成
  * セキュリティグループ (22, 80)

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

https://nodejs.org/en/download


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

## 2.2 Node.js Install

```sh
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash
. ~/.nvm/nvm.sh
nvm install --lts
node -v
```

## 2.2 build

```sh
npm cache clean --force
rm -rf node_modules
rm package-lock.json
npm install -g npm@latest
npm install
npm run build
```

<br>

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
sudo -E venv/bin/python app.py
```

<br>