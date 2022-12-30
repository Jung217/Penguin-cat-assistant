import requests
import pandas as pd
from io import StringIO
import datetime
import os
from bs4 import BeautifulSoup

message = input('請輸入股票名稱:')

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
    if(message == stock_ary[1]):
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

    print('\r')
    print('股票代碼：　' + stock_num)
    print('股票名稱：　' + message)
    print('證卷別　：　' + stock_atr)
    print('成交價　：　' + td_ary[10].text)
    print('昨收　　：　' + td_ary[11].text)
    print('漲跌價　：　' + td_ary[12].text)
    print('漲跌幅　：　' + td_ary[13].text)
    print('振幅　　：　' + td_ary[14].text)
    print('開盤　　：　' + td_ary[15].text)
    print('最高　　：　' + td_ary[16].text)
    print('最低　　：　' + td_ary[17].text)
    print('成交均價：　' + td_ary[22].text)

if(stock_name == False):
    print('\r')
    print('查無此股票，請再輸入一次')
    print('若股票名稱中有「臺」，請將它改為「台」')