from matplotlib.pyplot import pause
import pandas as pd
import requests
from bs4 import BeautifulSoup
from sqlalchemy import false, true
import datetime
def Stockchange(first,second):
    float(first)
    float(second)
    return (second-first)/first

Ticker = input('Choose Ticker')
url = 'https://finance.yahoo.com/quote/'+ Ticker +'?p='+ Ticker


html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'lxml')
stock_info  = soup.find('div', class_ = 'Bgc($bg-body) Mih(100%) W(100%) Bgc($layoutBgColor)! finance US')# finds the info on webpage that we care abput

#Stock Stats
stock_price = float(stock_info.find('fin-streamer', class_ = 'Fw(b) Fz(36px) Mb(-4px) D(ib)').text)


stock_changes = stock_info.find_all('fin-streamer', class_ ='Fw(500) Pstart(8px) Fz(24px)')
stock_percent_change = stock_changes[1].find('span').text
last_stockprice = 1.4
lasthigh = 1.425
lastLow = 1.410
stock_high = 1.465
LOSS_THRESHOLD = -0.05
initialbuy = 1.41
NegTrendThreshold = -0.01
PosTrendThreshold = 0.01
gain_threshold = 0.05
lastLow = 1.405
lastHigh =1.415
newLow = 1.405
newHigh=1.410
dec =false
inc = false
neutral = false

print(f''' Buy {Ticker} @ ${stock_price}''')

while true:
    stock_price = float(stock_info.find('fin-streamer', class_ = 'Fw(b) Fz(36px) Mb(-4px) D(ib)').text)
    x = Stockchange(initialbuy,stock_price)
    y = Stockchange(lasthigh,stock_price)
    if Stockchange(initialbuy,stock_price) < LOSS_THRESHOLD or Stockchange(lasthigh,stock_price) < NegTrendThreshold:
        print(f'''sell party city @ ${stock_price} ''')
        break
        

    #inc definition
    if stock_price > last_stockprice:
        inc = true
        dec = false
        neutral = false
        impulse = true
    elif stock_price < last_stockprice:
        dec = true
        inc = false
        neutral = false
    else:
        neutral =true
        dec =false
        inc = false

    if dec == true:
        newLow = stock_price
    if inc == true:
        newHigh = stock_price

    if newHigh > lastHigh:
        impulse = true
        pull_back =false
    #trend definition
    #trend
    if newLow > lastLow:
        uptrend = true
    else:
        uptrend=false
    if dec == true and uptrend == true:
        print(f'''buy party city @ ${stock_price} ''')
    elif inc == true and uptrend == true:
        print(f'''sell party city @ ${stock_price} ''')
    elif dec ==true and Stockchange(last_stockprice,stock_price) < NegTrendThreshold:
        print(f'''sell party city @ ${stock_price} ''')
    elif inc == true and Stockchange(last_stockprice,stock_price) > PosTrendThreshold:
        print(f'''buy party city @ ${stock_price} ''')
    elif neutral ==true:
        print('stay')
    elif Stockchange(initialbuy,stock_price) > gain_threshold:
        print(f'''sell party city @ ${stock_price} ''')
        break



    uptrend = false
    last_stockprice = stock_price
    lastLow = newLow
    newHigh = lastHigh
    pause()

print(stock_price)


#pull data from website, put data in spread sheet, if column has url paste link in column to activate code

