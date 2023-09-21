# 0 AWS

* S3作成
* IAMロール作成
* EC2作成

<br>

# 1 Gitでソースコードclone

```sh
sudo yum install -y git
git --version
git clone https://github.com/Tatsuki-Oike/aws_service.git
cd ./aws_service/05_S3
```

# 2 EC2とS3でデータのやり取り

```sh
export MY_BUCKET_NAME='bucket-name'
```

```sh
python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
pip3 install -r requirements.txt
```

```sh
python3 0_make_txt.py
python3 1_simple_upload.py
python3 2_url_upload.py
python3 3_simple_download.py
python3 4_url_download.py
python3 5_simple_delete.py
python3 6_url_delete.py
```
