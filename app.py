from flask import Flask, request, abort
from linbot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *

app = Flask(__name__)

line_bot_api = LineBotApi('8mHVNSHnlj3xx9180Kt+XKh6oVyljAhhV/qOrXL2XXorpdwIO5eard7Jfkvd2wR8P+cEQdUJQ3sEcI0clytSMsoaMH7fQZt4zjHoOUMdJXx9A9fsVr25H6gESwSPYJ3kOe3BF4+4qNnQzZXMVr5tbgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('fe4ffd95d0f99b968144e632168904cc')

line_bot_api.push_message('U9331f84776672cb357b3b8b9f89ebeaf', TextSendMessage(text='You can start !')) # Put your ID


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
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))


if lineMessage[0:3]== "隨便吃" :
    address=""
    lineMes =lineMessage
    if line[4:-1] == "":
        address = ""
    else:address =lineMes[4:1]
   addur1 = "htts://maps.googleapis.com/map/api/place/nearbyseach/json?key={}&address={}&sensor=false"
   .format(AIzaSyC5ahJJXTVNZPKaRWNS_Km_SyWIVzXOuDo,address)
   addressReq =request.get(addur1)
   addressDoc = addressReq.json()
   lat = addressDoc['result']['geometry']['location']['lat']
   lan = addressDoc['result']['geometry']['location']['lat']


    foodStoreSearch ="htts://maps.googleapis.com/map/api/place/nearbyseach/json?key={}&location={},{}&rankby=distance&type=restaurant&type=restaurant&language=zh-TW".format(AIzaSyC5ahJJXTVNZPKaRWNS_Km_SyWIVzXOuDo,lat,lng)

    foodReq =request.get(foodStoreSearch)
    nearby_restaurants_dict =foodReq.josn()
    top20_restaurants =nearby_restaurants_dict["results"]
    res_num =(len(top20_restaurants_dict))
    #取得評分高於3.9的店家位置
    bravo =[]
    for i in range(res_num):
        try:
            if top20_restaurants[i]['rating']>3.9:
                print('rate:',top20_restaurants[i]['rating'])
                bravo.append(i)
        except:
            KeyError
    if len(bravo)<0:
        content = '沒東西可吃'
        # restaurant =random.choice(top20_restaurants)沒有的話隨便一間
    #從高於3.9的店家隨幾選億間
    restaurant= top20_restaurants[random.choice(bravo)]
    #檢查餐廳有沒有照片，有的話顯示
    if restaurant.get('photos') is None:
        thumbnail_image_ur1 = None
    else:
    #根據文件，最多只會有一張照片
        photo_reference =restaurant['photos'][0]['photo_reference']
        photo_width =restaurant["photos"][0]["width"]
        thumbnail_image_ur1 =  "htts://maps.googleapis.com/map/api/place/photo?key={}&photoreference={}&maxwidth={}"
        .format（AIzaSyC5ahJJXTVNZPKaRWNS_Km_SyWIVzXOuDo,photo_reference,photo_width)
    #組裝餐廳詳細資訊
    rating = '無' if restaurant.get('rating') is None else restaurant['rating']
    address = '沒有資料' if restaurant.get('vicinity') is None else restaurant['vicinty']
    details = 'Google Map評分:{}\n地址:{}'.format(rating,address)
    #print(details)
    #取得餐廳的google map 網址
    map_url = "htts://www.google.com/maps/seach/?api=1&query={let},{long}&query_place_id={place_id}"
    .format(lat=restaurant['geometry']['location']['lat'],long=restaurant['geometry']['location']['lng'],place_id=restaurant['place_id'])

    # 回復使用 Buttons Template
    buttons_template =TemplateSendMessage(
    alt_text=restaurant["name"],
    template =ButtonsTemplate(
        thumbnail_image_ur1=thumbnail_image_ur1
        title =restaurant['name'],
        text=details,
        actions=[
            URITemplateAction(
                lable='查看地圖',
                uri=map_url
            ),
        ]
        )
        
    )
    line_bot_api.reply_message(event.reply_token, buttons_template)
return 0

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

