# 0 AWS

* VPC作成
  * パブリックサブネット2
  * プライベートサブネット2
  * NATゲートウェイ
* セキュリティグループ作成
  * port (3306)
* サブネットグループ作成
  * プライベートサブネット2
* パブリックにEC2インスタンス(WEBサーバー)作成
* RDS作成

<br>

# 1 RDB 接続

## 1.1 MariaDB Install

```sh
sudo yum update -y
sudo dnf install -y mariadb105-server
```

##  1.2 環境変数

* MYSQL_HOST = RDSのエンドポイント

```sh
export MYSQL_HOST='X.rds.amazonaws.com'
export MYSQL_USER='admin'
export MYSQL_PASSWORD='your_password'
export MYSQL_DATABASE='your_database'
```

## 1.3 RDS接続確認

```sh
mysql -h $MYSQL_HOST -u $MYSQL_USER -p
SHOW DATABASES;
exit
```

<br>

# 2 WEBアプリ

## 2.1 Gitでソースコードclone

```sh
sudo yum install -y git
git --version
git clone https://github.com/Tatsuki-Oike/aws_service.git
cd ./aws_service/04_RDS
```

## 2.2 Pythonの仮想環境構築

```sh
python3 -m venv venv # 仮想環境作成
source venv/bin/activate # 環境の中にはいる
python3 -m pip install --upgrade pip # pip upgrade
pip3 install -r requirements.txt # ライブラリインストール
```

## 2.3 Pythonの実行

```sh
sudo -E venv/bin/python app.py
```
