from flask import Flass
app = Flask(__name__)

import cv2 as cv
import numpy as np
from django.conf.urls.static import static
from django.conf import settings
from flask import Flask, request, abort
from linebot import  LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

line_bot_api = LineBotApi('8mHVNSHnlj3xx9180Kt+XKh6oVyljAhhV/qOrXL2XXorpdwIO5eard7Jfkvd2wR8P+cEQdUJQ3sEcI0clytSMsoaMH7fQZt4zjHoOUMdJXx9A9fsVr25H6gESwSPYJ3kOe3BF4+4qNnQzZXMVr5tbgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('fe4ffd95d0f99b968144e632168904cc')

@app.route("/image_process", methods=['POST'])
def image_process(image_name,image_path):
    if event.message.type=='image':
        image_name = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(4))
        image_content = line_bot_api.get_message_content(event.message.id)
        image_name = image_name.upper()+'.jpg'
        path='./static/'+image_name
    with open(path, 'wb') as fd:
        for chunk in image_content.iter_content():
            fd.write(chunk)
    img = cv.imread(image_path)#讀取照片原圖
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)#將原圖轉為灰階圖
    ret,binary=cv.threshold(gray,127,255,cv.THRESH_BINARY)#將灰階圖進行二值化處理
    gray_path = './static/gray_'+image_name#將灰階圖與二值化處理圖存為實體檔案
    binary_path = './static/binary_'+image_name
    cv.imwrite(gray_path,gray)
    cv.imwrite(binary_path,binary)
    return gray_path, binary_path

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))

if __name__ == '__main__':
    app.run()