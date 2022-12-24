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
    if "股票 " in message:
         buttons_template_message = TemplateSendMessage(
         alt_text = "股票資訊",
        template=CarouselTemplate( 
            columns=[ 
                    CarouselColumn( 
                        thumbnail_image_url ="https://www.google.com/url?sa=i&url=https%3A%2F%2Flure.tw%2F%3Fc%3DProducts%26act%3DDetail%26id%3D1294406&psig=AOvVaw2lyI6lR83vdHnXQWtR0Ij-&ust=1671982271391000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCPCAz7zJkvwCFQAAAAAdAAAAABAL",
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
         line_bot_api.reply_message(event.reply_token, TextSendMessage(message))

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)