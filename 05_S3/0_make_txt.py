import os

# フォルダとファイル
download_folder = "s3_txt"
download_file = os.path.join(
    download_folder,
    "sample.txt"
)
os.makedirs(download_folder, exist_ok=True)

# ファイルを作成し、中身を書き込む
with open(download_file, 'w') as file:
    file.write('Hello, World')

print("Done")