message = "@股票 台積電"

if '@股票' in message:
    stock_in = message.replace('@股票 ', '')
    stock_info(stock_in)
    remessage = stock_in
    print(remessage)

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