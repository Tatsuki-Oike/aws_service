# 0 AWS

* VPC作成
  * パブリックサブネット2
  * プライベートサブネット2
* S3作成
  * パブリックアクセスをすべてブロック オフ
  * バケットポリシー変更
  * Cross-Origin Resource Sharing (CORS)
  * IAMロール作成
* EC2作成
  * セキュリティグループ (22, 80)
* RDS作成
  * セキュリティグループ作成(3306)
  * サブネットグループ作成
    * プライベートサブネット2
  * RDS作成

<br>
バケットポリシー変更

```js
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicRead",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::bucket-name/*"
        }
    ]
}
```

<br>
Cross-Origin Resource Sharing (CORS)

```js
[
    {
        "AllowedHeaders": [
            "*"
        ],
        "AllowedMethods": [
            "PUT"
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
cd ./aws_service/07_S3_RDS_WEB
npm init vite-app frontend
cd frontend
npm install
npm install axios
npm install vue-router
npm install vuex
npm run dev
```

```sh
npm run build
```

<br>

# 2 RDS 接続

## 2.1 MariaDB Install

```sh
sudo yum update -y
sudo dnf install -y mariadb105-server
```

##  2.2 環境変数

* MYSQL_HOST = RDSのエンドポイント

```sh
export MYSQL_HOST='X.rds.amazonaws.com'
export MYSQL_USER='admin'
export MYSQL_PASSWORD='your_password'
export MYSQL_DATABASE='your_database'
```

## 2.3 RDS接続確認

```sh
mysql -h $MYSQL_HOST -u $MYSQL_USER -p
SHOW DATABASES;
exit
```

<br>

# 3 Frontend

## 3.1 ソースコード clone

```sh
sudo yum install -y git
git --version
git clone https://github.com/Tatsuki-Oike/aws_service.git
cd ./aws_service/07_S3_RDS_WEB/frontend
```

## 3.2 Node.js Install

```sh
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash
. ~/.nvm/nvm.sh
nvm install --lts
node -v
```

## 3.3 build

```sh
npm cache clean --force
rm -rf node_modules
rm package-lock.json
npm install -g npm@latest
npm install
npm run build
```

<br>

# 4 Backend

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
