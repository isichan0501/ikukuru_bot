mkdir images
mkdir secrets
mkdir logs
touch .env

#undetected_chromedriverのフォーク版
pip install -U git+https://github.com/sebdelsol/undetected-chromedriver.git


cd BotHelper
curl -O https://chromedriver.storage.googleapis.com/95.0.4638.69/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
rm chromedriver_linux64.zip