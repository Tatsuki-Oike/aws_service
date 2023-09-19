# 0 AWSサービス

* EC2の作成
  * セキュリティグループ(22, 80)

<br>

# 1 DBサーバー

## 1.1 MariaDB Install

```sh
sudo yum update -y
sudo dnf install -y mariadb105-server
sudo systemctl start mariadb
sudo systemctl enable mariadb
```

## 1.2 環境変数

```sh
export MYSQL_HOST='localhost'
export MYSQL_USER='root'
export MYSQL_PASSWORD='your_password'
export MYSQL_DATABASE='your_database'
```

## 1.3 データベース設定

```sh
sudo mysqladmin -u root password $MYSQL_PASSWORD
mysqladmin -u root -p create $MYSQL_DATABASE
mysql -u root -p -e "SHOW DATABASES;"
```

<br>

# 2 WEBアプリ 

## 2.1 Gitでソースコードclone

```sh
sudo yum install -y git
git --version
git clone https://github.com/Tatsuki-Oike/aws_service.git
cd ./aws_service/01_EC2_DB
```

## 2.2 Pythonの仮想環境構築

```sh
python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
pip3 install -r requirements.txt
```

## 2.3 Pythonの実行

```sh
sudo -E venv/bin/python app.py
```
