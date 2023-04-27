# ikukuru_bot

# .env


create dirs(secrets, logs, images).
Create .env file and define the following environment variables.

###
SHEET_JSON_FILE=secrets/〇〇
SHEET_KEY=〇〇
SHEET_NAME=〇〇
API_URL=〇〇
CHROME_PROFILE_DIR=ChromeProfile
LINE_API_TOKEN=〇〇
IMG_DIR=images
BUCKET_NAME=〇〇


Add the spreadsheet API token file (.json) used by the gspread library to the secrets directory.

BUCKET_NAME is the name of the s3 bucket where the image is stored.

SHEET_KEY is the key of the spreadsheet where the template is saved


setup.sh for amazonlinux



# chatgptで返答する
3回以上会話のラリーが続いたらメアド聞く仕様にする
自分と相手の情報を事前に取得