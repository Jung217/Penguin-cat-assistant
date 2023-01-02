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

def glucose_graph(client_id, imgpath):
	im = pyimgur.Imgur(client_id)
	upload_image = im.upload_image(imgpath, title="Uploaded with PyImgur")
	return upload_image.link

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
        stock_out = ('日期　　：　%s\n股票代碼：　%s\n股票名稱：　%s\n證卷別　：　%s\n成交價　：　%s\n昨收　　：　%s\n漲跌價　：　%s\n漲跌幅　：　%s\n振幅　　：　%s\n開盤價　：　%s\n最高價　：　%s\n最低價　：　%s\n成交均價：　%s' %(date, stock_num, stock_in, attribute, price, yesterday, updowmprice, updownchange, amplitude, openprice, highprice, lowprice, averageprice))
        
    elif(stock_name == False):
        stock_out = '查無此股票，請再輸入一次' + '\n' + '若股票名稱中有「臺」，請將它改為「台」'
    return stock_out

def glucose_graph(client_id, imgpath):
	im = pyimgur.Imgur(client_id)
	upload_image = im.upload_image(imgpath, title="Uploaded with PyImgur")
	return upload_image.link

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
    if event.message.type == "image":
        message_content = line_bot_api.get_message_content(event.message.id)

        file_path = "Penguin-cat-assistant\pic"

        with open(file_path, 'wb') as fd:
            for chunk in message_content.iter_content():
                fd.write(chunk)

        line_bot_api.reply_message(event.reply_token,TextSendMessage(str(message_content)))

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)