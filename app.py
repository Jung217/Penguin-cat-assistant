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
    if re.match("大秘寶",message):
        remessage = remessage = "觸發驚喜的密語:\n\n攝影\n恭喜\n今天我生日\n金門大學在哪\n\n試著輸入看看吧!"
        line_bot_api.reply_message(event.reply_token,TextSendMessage(remessage))
    elif "生日" in message:
        bless = ['生日快樂！希望你的所有願望都能成真','準備好開始倒數了嗎？下次跟你說生日快樂是 365 天之後，生日快樂！','原本想送你一個最可愛的禮物，後來只能找第二可愛的，因為你排名第一呀。','大壽星，小蛋糕，絕配。生日快樂！','你生日的這一天，我沒有跟你在一起，只希望你能快樂、健康、美麗，生命需要奮鬥、創造和把握！生日快樂！','Happy birthday to the most wonderful friend in my heart.','Wish you a happy birthday! May the best and the loving things be some of the joy your birthday bring.']
        line_bot_api.reply_message(event.reply_token,TextSendMessage(bless[random.randint(0, len(bless)-1)]))
    elif "恭喜" in message:
        sticker_message = StickerSendMessage(
            package_id='6325',
            sticker_id='10979924'
        )
        line_bot_api.reply_message(event.reply_token, sticker_message)
    elif re.match("金門大學在哪",message):
        location_message = LocationSendMessage(
            title= "國立金門大學", 
            address= "892金門縣金寧鄉大學路1號",
            latitude= 24.44829638687612,  
            longitude= 118.32249208222159
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif "股票 " in message:
        buttons_template_message = TemplateSendMessage(
        alt_text = "股票資訊",
        template=CarouselTemplate(
            columns=[
                CarouselColumn( 
                    thumbnail_image_url ="https://chenchenhouse.com//wp-content/uploads/2020/10/%E5%9C%96%E7%89%871-2.png",
                    title = message + " 股票資訊", 
                    text ="請點選想查詢的股票資訊", 
                    actions =[
                        MessageAction( 
                            label= message[3:] + " 個股資訊",
                            text= "個股資訊 " + message[3:]),
                        MessageAction( 
                            label= message[3:] + " 個股新聞",
                            text= "個股新聞 " + message[3:])
                        ]
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template_message)
    else:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(message))

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)