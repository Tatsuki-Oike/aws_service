# 0 AWS

* VPC作成
  * パブリックサブネット1
  * プライベートサブネット1
  * NATゲートウェイ
* パブリックにWEBサーバー用のEC2作成
  * セキュリティグループ(22, 80)
* ブライベートにDBサーバー用のEC2作成
  * セキュリティグループ(22, 3306)

<br>
.ssh/config

```sh
Host webssh
    HostName X.X.X.X # (WEBサーバ-のパブリックIP)
    User ec2-user
    Port 22
    IdentityFile ~/.ssh/X.pem # キーファイルのパス

Host dbssh
    HostName X.X.X.X # (DBサーバ-のプライベートIP)
    User ec2-user
    Port 22
    IdentityFile ~/.ssh/X.pem # キーファイルのパス
    ProxyCommand ssh -W %h:%p webssh
```

<br>

# 1 DBサーバー

## 1.1 MariaDB Install

```sh
sudo yum update -y
sudo dnf install -y mariadb105-server
sudo systemctl start mariadb
sudo systemctl enable mariadb
```

## 1.2 データベース設定

```sh
sudo mysqladmin -u root password your_root_password
mysql -u root -p
```

<br>
X.X.X.X = WEBサーバーのプライベートIP

```sh
CREATE DATABASE your_database;
SHOW DATABASES;
SELECT user, host FROM mysql.user;
GRANT ALL PRIVILEGES ON *.* TO 'web_user'@'X.X.X.X' IDENTIFIED BY 'web_user_pass';
FLUSH PRIVILEGES;
SELECT user, host FROM mysql.user;
exit
```

```sh
sudo systemctl restart mariadb
```

<br>

# 2 WEBサーバー

## 2.1 MariaDB Install

```sh
sudo yum update -y
sudo dnf install -y mariadb105-server
```

##  2.2 環境変数

<br>
MYSQL_HOST = DBサーバーのプライベートIP

```sh
export MYSQL_HOST='X.X.X.X'
export MYSQL_USER='web_user'
export MYSQL_PASSWORD='web_user_pass'
export MYSQL_DATABASE='your_database'
```

## 2.3 データベース設定

```sh
mysql -h $MYSQL_HOST -u $MYSQL_USER -p
SHOW DATABASES;
exit
```

<br>

# 3 WEBアプリ

## 3.1 Gitでソースコードclone

```sh
sudo yum install -y git
git --version
git clone https://github.com/Tatsuki-Oike/aws_service.git
cd ./aws_service/03_PRIVATE_DB
```

## 3.2 Pythonの仮想環境構築

```sh
python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
pip3 install -r requirements.txt
```

## 3.3 Pythonの実行

```sh
sudo -E venv/bin/python app.py
```
