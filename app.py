from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
import re
import os
import random

app = Flask(__name__)

line_bot_api = LineBotApi('8mHVNSHnlj3xx9180Kt+XKh6oVyljAhhV/qOrXL2XXorpdwIO5eard7Jfkvd2wR8P+cEQdUJQ3sEcI0clytSMsoaMH7fQZt4zjHoOUMdJXx9A9fsVr25H6gESwSPYJ3kOe3BF4+4qNnQzZXMVr5tbgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('fe4ffd95d0f99b968144e632168904cc')

line_bot_api.push_message('U9331f84776672cb357b3b8b9f89ebeaf', TextSendMessage(text='You can start !'))


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
 
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
 
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = event.message.text
    if re.match("今天我生日",message):
        bless = ['生日快樂！希望你的所有願望都能成真','準備好開始倒數了嗎？下次跟你說生日快樂是 365 天之後，生日快樂！','原本想送你一個最可愛的禮物，後來只能找第二可愛的，因為你排名第一呀。','大壽星，小蛋糕，絕配。生日快樂！','你生日的這一天，我沒有跟你在一起，只希望你能快樂、健康、美麗，生命需要奮鬥、創造和把握！生日快樂！','Happy birthday to the most wonderful friend in my heart.','Wish you a happy birthday! May the best and the loving things be some of the joy your birthday bring.']
        line_bot_api.reply_message(event.reply_token,TextSendMessage(bless[random.randint(0, len(bless)-1)]))
    elif re.match("恭喜",message):
        sticker_message = StickerSendMessage(
            package_id='6325',
            sticker_id='10979924'
        )
        line_bot_api.reply_message(event.reply_token, sticker_message)
    else:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(message))

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)