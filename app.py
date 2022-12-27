from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
import re
import os
import random
import configparser

app = Flask(__name__)

config = configparser.ConfigParser()
config.read('config.ini')

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
    sendString = ""
    if re.match("大秘寶",message):
        remessage = remessage = "觸發驚喜的密語:\n\n後製\n恭喜\n今天我生日\n金門大學在哪\n\n試著輸入看看吧!"
        line_bot_api.reply_message(event.reply_token,TextSendMessage(remessage))
    elif "擲筊" in event.message.text:
        sendString = divinationBlocks()
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=sendString))
    elif "抽籤" in event.message.text:
        sendString = drawStraws()
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=sendString))
    elif "生日" in message:
        bless = ['生日快樂！希望你的所有願望都能成真','準備好開始倒數了嗎？下次跟你說生日快樂是 365 天之後，生日快樂！','原本想送你一個最可愛的禮物，後來只能找第二可愛的，因為你排名第一呀。','大壽星，小蛋糕，絕配。生日快樂！','你生日的這一天，我沒有跟你在一起，只希望你能快樂、健康、美麗，生命需要奮鬥、創造和把握！生日快樂！','Happy birthday to the most wonderful friend in my heart.','Wish you a happy birthday! May the best and the loving things be some of the joy your birthday bring.']
        line_bot_api.reply_message(event.reply_token,TextSendMessage(bless[random.randint(0, len(bless)-1)]))
    elif "吃什麼" in message:
        restaurant = [['金門牛家莊','金門縣金城鎮民族路318巷5號',24.431038009052358,118.31409884232771],['記德海鮮餐廳','金門縣金寧鄉慈湖路二段105號',24.447731288894147,118.31104168283404],["閩式燒餅專賣店","金門縣金沙鎮博愛街48號",24.490208447308117, 118.41312079817922],["蚵嗲之家", '金門縣金城鎮莒光路一段59號' ,24.4315964744328, 118.31846009817842],["良金牧場(良金牛肉麵)", '金門縣金湖鎮金湖鎮漁村160號', 24.437400125726505, 118.40650035380833],['合泉購物中心' ,'金門縣金湖鎮小徑村63號' ,24.449582351890776, 118.38542601147971],['泉民水果創作料理' ,'金門縣金寧鄉伯玉路二段224巷8號' ,24.441130927810175, 118.33799841147962],['米香屋廣東粥', '金門縣金城鎮民生路21號', 24.434645106470853, 118.31949205380819],['佳軒西點麵包店', '金門縣金城鎮光前路89號', 24.433793499832237, 118.31425455380818],['談天樓' ,'金門縣金湖鎮復興路3號', 24.440858867513338, 118.41693036915065],['永春廣東粥', '金門縣金城鎮莒光路162之1號', 24.433998175331006, 118.31611541147943],['老爹牛肉麵' ,'金門縣金湖鎮武德新莊26號', 24.440601898161827, 118.41368335565755],['集成餐廳', '金門縣金城鎮中興路8號', 24.432412613828625, 118.31645979983567],['遠來興小吃店', '金門縣三民路22巷11號', 24.490419774273132, 118.41309336915134],['石碇公臭臭鍋','金門店金門縣光前路50號' ,24.43280813684032, 118.3156548673014],['加州咖啡屋', '金門縣金城鎮珠浦南路74巷21號', 24.432258109799943, 118.31467924216442],['麵屋無粹 MuIki', '金門縣金城鎮環島北路一段126號', 24.44301319125692, 118.3249999691508],['進麗小籠包', '金門縣金城鎮光前路34號', 24.4324114180819, 118.31615398264381],['龍河廣東粥', '金門縣金城鎮光前路38之3號', 24.43250226910213, 118.31604159613701],['長合餅店', '金門縣金沙鎮三民路24號', 24.490198147322072, 118.4126813538088],['愜意甜點工作室' ,'金門縣金沙鎮後浦頭60號', 24.487384496657867, 118.4136365403157],['聯成廣東粥', '金門縣金城鎮民生路45巷1號', 24.43574714057928, 118.31885666915078],['三層樓芋頭餐館', '金門縣烈嶼鄉黃厝23之1號', 24.446615420930428, 118.25218372682207],['山西拌麵長榮商行', '金門縣金沙鎮三山村山西22號', 24.891895879566814, 118.49611120953122],['俊輝碳烤' ,'金門縣金湖鎮新湖裏新頭99號', 24.43393396765973, 118.41903772682178],['高坑牛肉乾', '金門縣金沙鎮高坑38號', 24.467145257282436, 118.39391824031554],['浯州廚藝鐵板燒', '金門縣金城鎮民權路124號', 24.435841201361846, 118.31681588264378],['京采包子饅頭', '金門縣民權路71號', 24.43296517274044, 118.31439315565754],['永寬鹹粿店', '金門縣金城鎮莒光路一段44號', 24.431675683167654, 118.31859426915055],['喬安牧場伯玉旗艦店', '金門縣金寧鄉伯玉路二段297號', 24.440889730337027, 118.33981109613705],['後浦泡茶間 Local Teahouse', '金門縣金城鎮莒光路122號' ,24.433155136463913, 118.31660188264397],['喜相逢小吃店', '金門縣金湖鎮復興路5號', 24.440834965264987, 118.41695918449318],['順天洋樓－自然茶 咖啡(歐陽鐘遠洋樓) ','金門縣金城鎮歐厝50號', 24.408164903471416, 118.33152865380795],['樸食 À table ','金門縣金城鎮中興路205巷6號', 24.43493527029771, 118.32023126915065],['金門背貓客', '金門縣金沙鎮後珩4號', 24.509926104804446, 118.40769381332957],['金門蛋捲', '金門縣金城鎮莒光路一段42號', 24.431490201974047, 118.31856966915055],['壽記廣東粥' ,'金門縣金寧鄉伯玉路一段216之1號' ,24.43579806578197, 118.32740794031518],['9號讚','金門縣金湖鎮復興路7號', 24.440756158499198, 118.41693728449324],['山外不一樣雞排', '金門縣金湖鎮新市裏中正路26號', 24.440850828113994, 118.41607721147955],['榕榕園麵館', '金門縣金湖鎮黃海路7號', 24.443215094516106, 118.41475524216446],['御饌屋 みけや', '金門縣金城鎮西門裏富康一村9巷18號', 24.43852619543079, 118.32116435380823],['巴布咖啡屋(酸白菜水餃專賣店)', '金門縣金湖鎮復興路92號', 24.442105161407245, 118.41516025380825],['阿芬海產店' , '金門縣金湖鎮復國墩25號', 24.44841818725616, 118.47000838264404],['帕堤-Lets party', '金門縣金城鎮西海路3段72巷3弄5號', 24.420171367388107, 118.30931381147938],['三寶齋', '金門縣金城鎮模範街10號' ,24.432126037580243, 118.31927591332865],['雨川食堂'  ,'893金門縣金城鎮莒光路53號', 24.43220143749837, 118.31755385380826],['吉祥餐飲', '893金門縣金城鎮中興路143號', 24.433844692009302, 118.31849788264392],['金門 阿公ㄟ手工豆花', '金門縣金城鎮模範街15號', 24.431824256717064, 118.31932367099981]]
        r = random.randint(0, len(restaurant)-1)
        location_message = LocationSendMessage(
            title= restaurant[r][0], 
            address= restaurant[r][1],
            latitude= restaurant[r][2],  
            longitude= restaurant[r][3]
        )
        line_bot_api.reply_message(event.reply_token, location_message)
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
    elif "後製" in message:
        buttons_template_message = TemplateSendMessage(
        alt_text = "後製",
        template=CarouselTemplate( 
            columns=[ 
                CarouselColumn( 
                    thumbnail_image_url ="https://live.staticflickr.com/65535/52288829887_98585c5641_h.jpg",
                    title = message + " 這裡看", 
                    text ="請點選想了解的資訊", 
                    actions =[
                        MessageAction( 
                            label="Flickr",
                            text="https://www.flickr.com/photos/cjc217"),
                        MessageAction( 
                            label="Instagram",
                            text="https://www.instagram.com/chih_jung_chien/")
                        ]
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template_message)
    else:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(message))

def divinationBlocks():
    divinationBlocksList = ["笑杯", "正杯", "正杯", "笑杯"] 
    return divinationBlocksList[random.randint(0, len(divinationBlocksList) - 1)]

def drawStraws():
    drawStrawsList = ["大吉", "中吉", "小吉", "吉", "凶", "小凶", "中凶", "大凶"]
    return drawStrawsList[random.randint(0, len(drawStrawsList) - 1)]

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)