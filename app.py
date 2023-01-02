from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
from io import StringIO
from bs4 import BeautifulSoup
import datetime
import pandas as pd
import requests
import re
import os
import random
import configparser
from PIL import Image
import pyimgur

app = Flask(__name__)

config = configparser.ConfigParser()
config.read('config.ini')

line_bot_api = LineBotApi('8mHVNSHnlj3xx9180Kt+XKh6oVyljAhhV/qOrXL2XXorpdwIO5eard7Jfkvd2wR8P+cEQdUJQ3sEcI0clytSMsoaMH7fQZt4zjHoOUMdJXx9A9fsVr25H6gESwSPYJ3kOe3BF4+4qNnQzZXMVr5tbgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('fe4ffd95d0f99b968144e632168904cc')

line_bot_api.push_message('U9331f84776672cb357b3b8b9f89ebeaf', TextSendMessage(text='You can start !'))
line_bot_api.push_message('U1d8c4bfd627123ece1085e294e45ddee', TextSendMessage(text='You can start !'))

def divinationBlocks():
    divinationBlocksList = ["笑杯", "聖杯", "聖杯", "無杯", "笑杯", "聖杯", "聖杯", "無杯", "笑杯", "聖杯", "聖杯", "無杯", "笑杯", "聖杯", "聖杯", "無杯", "笑杯", "聖杯", "聖杯", "無杯", "笑杯", "聖杯", "聖杯", "無杯", "笑杯", "聖杯", "聖杯", "無杯", "笑杯", "聖杯", "聖杯", "無杯", "笑杯", "聖杯", "聖杯", "無杯", "笑杯", "聖杯", "聖杯", "無杯", "笑杯", "聖杯", "聖杯", "無杯", "笑杯", "聖杯", "聖杯", "無杯", "笑杯", "聖杯", "聖杯", "無杯", "笑杯", "聖杯", "聖杯", "無杯", "笑杯", "聖杯", "聖杯", "無杯", "笑杯", "聖杯", "聖杯", "無杯", "笑杯", "聖杯", "聖杯", "無杯", "笑杯", "聖杯", "聖杯", "無杯", "笑杯", "聖杯", "聖杯", "無杯", "笑杯", "聖杯", "聖杯", "無杯", "笑杯", "聖杯", "聖杯", "無杯", "笑杯", "聖杯", "聖杯", "無杯", "笑杯", "聖杯", "聖杯", "無杯", "笑杯", "聖杯", "聖杯", "無杯", "笑杯", "聖杯", "聖杯", "無杯", "超罕見立杯"] 
    return divinationBlocksList[random.randint(0, len(divinationBlocksList) - 1)]

def drawStraws():
    drawStrawsList = ["大吉", "中吉", "小吉", "吉", "凶", "小凶", "中凶", "大凶", "大吉", "中吉", "小吉", "吉", "凶", "小凶", "中凶", "大凶"]
    return drawStrawsList[random.randint(0, len(drawStrawsList) - 1)]

def stock_info(stock_in):
    url = 'https://isin.twse.com.tw/isin/class_main.jsp?owncode=&stockname=&isincode=&market=1&issuetype=&industry_code=&Page=1&chklike=Y'
    r = requests.get(url)
    listed = pd.read_html(r.text)[0]
    listed.columns = listed.iloc[0,:]

    stock_name = True
    for i in range(24743):
        stock_ary = []
        stock_ary.append(listed.iloc[i][2])
        stock_ary.append(listed.iloc[i][3])
        stock_ary.append(listed.iloc[i][5])
        if(stock_in == stock_ary[1]):
            stock_num = stock_ary[0]
            stock_atr = stock_ary[2]
            stock_name = True
            break
    else:
        stock_name = False
    
    if(stock_name == True):
        url_stock = ('https://goodinfo.tw/tw/StockBzPerformance.asp?STOCK_ID=%s' %stock_num)
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
        }
        r1 = requests.get(url_stock, headers=headers)
        r1.encoding = "utf-8"

        sp = BeautifulSoup(r1.text,'lxml')
        rows = sp.select('table.b1.p4_2.r10 tr')

        td_ary = []
        for row in rows:
            td = row.find_all('td')
            td_ary += td

        if(stock_atr == '股票'):
            date = td_ary[4].text.replace('資料日期: ', '')  #日期
            stock_num = stock_num                           #股票代碼
            stock_in = stock_in                             #股票名稱
            attribute = stock_atr                           #證卷別
            price = td_ary[10].text                         #成交價
            yesterday = td_ary[11].text                     #昨收
            updowmprice = td_ary[12].text                   #漲跌價
            updownchange = td_ary[13].text                  #漲跌幅
            amplitude = td_ary[14].text                     #振幅
            openprice = td_ary[15].text                     #開盤價
            highprice = td_ary[16].text                     #最高價
            lowprice = td_ary[17].text                      #最低價
            averageprice = td_ary[22].text                  #成交均價

        else:
            date = td_ary[1].text.replace('資料日期: ', '')  
            stock_num = stock_num                           
            stock_in = stock_in                         
            attribute = stock_atr                       
            price = td_ary[4].text                      
            yesterday = td_ary[5].text                
            updowmprice = td_ary[6].text                
            updownchange = td_ary[7].text               
            amplitude = td_ary[8].text                 
            openprice = td_ary[9].text                     
            highprice = td_ary[10].text                    
            lowprice = td_ary[11].text                     
            averageprice = td_ary[16].text      

        stock_out = ('日期　　：　%s\n股票代碼：　%s\n股票名稱：　%s\n證卷別　：　%s\n成交價　：　%s\n昨收　　：　%s\n漲跌價　：　%s\n漲跌幅　：　%s\n振幅　　：　%s\n開盤價　：　%s\n最高價　：　%s\n最低價　：　%s\n成交均價：　%s' %(date, stock_num, stock_in, attribute, price, yesterday, updowmprice, updownchange, amplitude, openprice, highprice, lowprice, averageprice))
        
    elif(stock_name == False):
        stock_out = '查無此股票，請再輸入一次' + '\n' + '若股票名稱中有「臺」，請將它改為「台」'
    return stock_out

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

@handler.add(MessageEvent)
def handle_message(event):
    message = event.message.text
    sendString = ""
    
    if re.match("大秘寶",message):
        remessage = "觸發驚喜的密語:\n\n恭喜\n今天我生日\n金門大學在哪\n\n試著輸入看看吧!"
        line_bot_api.reply_message(event.reply_token,TextSendMessage(remessage))

    elif "生日" in message:
        bless = ['生日快樂！希望你的所有願望都能成真','準備好開始倒數了嗎？下次跟你說生日快樂是 365 天之後，生日快樂！','原本想送你一個最可愛的禮物，後來只能找第二可愛的，因為你排名第一呀。','大壽星，小蛋糕，絕配。生日快樂！','你生日的這一天，我沒有跟你在一起，只希望你能快樂、健康、美麗，生命需要奮鬥、創造和把握！生日快樂！','Happy birthday to the most wonderful friend in my heart.','Wish you a happy birthday! May the best and the loving things be some of the joy your birthday bring.']
        line_bot_api.reply_message(event.reply_token,TextSendMessage(bless[random.randint(0, len(bless)-1)]))

    elif re.match("股票資訊",message):
        remessage = "請輸入您想輸入的股票名稱: \n 如:@台積電 \n 請稍後..."
        line_bot_api.reply_message(event.reply_token,TextSendMessage(remessage))
        
    elif '@' in message:
        stock_in = message.replace('@', '')
        remessage = stock_info(stock_in)
        line_bot_api.reply_message(event.reply_token,TextSendMessage(remessage))

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

    elif re.match("運勢",message):
        buttons_template_message = TemplateSendMessage(
        alt_text = "運勢",
        template=CarouselTemplate( 
            columns=[ 
                CarouselColumn( 
                    thumbnail_image_url ="https://mednote.files.wordpress.com/2019/10/img_1689.jpg",
                    title = "讓貓貓企鵝小助手\n為你測試運氣吧!", 
                    text ="請選擇一種方法測", 
                    actions =[
                        MessageAction( 
                            label="擲筊",
                            text="擲筊"),
                        MessageAction( 
                            label="抽籤",
                            text="抽籤"),
                        MessageAction( 
                            label="星座",
                            text="星座運勢")
                        ]
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template_message)

    elif re.match("成品展示",message):
        sendString = "https://drive.google.com/drive/folders/16puql_Nj0VeFBt3a24JzD8N4akAcw8LK?usp=sharing"
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=sendString))

    elif re.match("更多特效",message):
        sendString = "https://github.com/Jung217/Penguin-cat-assistant/tree/main/public"
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=sendString))

    elif re.match("後製特效",message):
        sendString = "https://colab.research.google.com/drive/1zuaIM3YK3jbfLykKOtk5fr8j6fLkT3Ce?authuser=2#scrollTo=TEBFojJ3hB27 \n\n https://youtu.be/Tp_tT4vJIdY"
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=sendString))

    elif re.match("擲筊",message):
        sendString = "恭喜" + divinationBlocks() + "!"
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=sendString))

    elif re.match("抽籤",message):
        sendString = "恭喜" + drawStraws() + "!"
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=sendString))

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
                            label="後製",
                            text="後製特效"),
                        MessageAction( 
                            label="更多",
                            text="更多特效"),
                        MessageAction( 
                            label="成品",
                            text="成品展示")
                        ]
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template_message)

    elif re.match("更多功能",message):
        image_message = ImageSendMessage(
            original_content_url='https://raw.githubusercontent.com/Jung217/Penguin-cat-assistant/main/pic/tired.jpg',
            preview_image_url='https://raw.githubusercontent.com/Jung217/Penguin-cat-assistant/main/pic/tired.jpg'
        )
        line_bot_api.reply_message(event.reply_token, image_message)

    elif re.match("星座運勢",message):
        remessage = "請輸入星座代號:\n0.牡羊 1.金牛 2.雙子\n3.巨蟹 4.獅子 5.處女\n6.天秤 7.天蠍 8.射手\n9.魔羯 10.水瓶 11.雙魚"
        line_bot_api.reply_message(event.reply_token,TextSendMessage(remessage))

    elif re.match("0",message) or re.match("1",message) or re.match("2",message) or re.match("3",message) or re.match("4",message) or re.match("5",message) or re.match("6",message) or re.match("7",message) or re.match("8",message) or re.match("9",message) or re.match("10",message) or re.match("11",message):
        message_int = int(message)
        if(message_int >= 0 and message_int <= 11):
            remessage = "https://astro.click108.com.tw/daily_"+ message + ".php?iAstro=" + message
            line_bot_api.reply_message(event.reply_token,TextSendMessage(remessage))
        else:
            remessage = '請再輸入一次星座代號!'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(remessage))

    else:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(message))

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)