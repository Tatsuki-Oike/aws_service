# 0 AWS

* VPC作成
  * パブリックサブネット2
  * プライベートサブネット2
  * NATゲートウェイ
* S3作成
  * パブリックアクセスをすべて ブロック オフ
  * バケットポリシー変更
  * Cross-Origin Resource Sharing (CORS)
  * IAMロール作成
* EC2作成
  * セキュリティグループ (22, 80, 5000)
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

```sh
sudo yum install -y git
git --version
git clone https://github.com/Tatsuki-Oike/aws_service.git
cd ./aws_service/07_S3_RDS_WEB/frontend
```

```sh
sudo yum install httpd -y # Apache Install
sudo systemctl start httpd # Apache 起動
sudo cp -r dist/* /var/www/html # WEBアプリフォルダ移動
```

# 4 Backend

```sh
cd ../backend
python3 -m venv venv # 仮想環境作成
source venv/bin/activate # 環境の中にはいる
python3 -m pip install --upgrade pip # pip upgrade
pip3 install -r requirements.txt # ライブラリインストール
sudo -E venv/bin/python app.py
```

<br>
