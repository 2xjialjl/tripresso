import requests
from lxml import etree
import pandas as pd
import pymysql
conn = pymysql.connect(host='localhost',port=3306,user='root',password='', db='trip', charset='utf8')
cursor = conn.cursor()
go_date_list = []
title_list = []
find_play_day_list = []
find_pay_list = []
find_total_list = []
find_but_list = []
for f in range(1, 6):
    url = 'https://www.4p.com.tw/EW/GO/GroupList.asp?pageGO='+str(f)+'&tabList=GO&regmCd=0009'
    html = requests.get(url)
    soup = etree.HTML(html.text)
    #  ###出發日期###
    find_go_date = soup.xpath('//*[@id="listDataGO"]//div/div//div[6]')
    for i in find_go_date:
        go_date = i.text.replace(' (一)', '').replace(' (二)', '').replace(' (三)', '').replace(' (四)', '').replace(' (五)', '').replace(' (六)', '').replace(' (日)', '')
        go_date_list.append(go_date)
    #  ###出發日期###

    #  ###行程名稱###
    find_title = soup.xpath('//*[@id="listDataGO"]//div/div//div[3]/a/text()')
    for j in find_title:
        title = j.strip()
        title_list.append(title)
    title_list = list(filter(None, title_list))
    #  ###行程名稱###

    #  ###旅遊天數###
    find_play_day = soup.xpath('//*[@id="listDataGO"]//div/div//div[5]')
    for m in find_play_day:
        play_day = m.text.replace('天', '')
        find_play_day_list.append(play_day)
    #  ###旅遊天數###

    #  ###價錢###
    find_pay = soup.xpath('//*[@id="listDataGO"]//div/div//div[8]/span/strong')
    for w in find_pay:
        pay = w.text.replace(',', '')
        find_pay_list.append(pay)
    #  ###價錢###

    #  ###總團位###
    find_total = soup.xpath('//*[@id="listDataGO"]//div/div//div[9]//span[2]')
    for o in find_total:
        total = o.text
        find_total_list.append(total)
    #  ###總團位###

    #  ###可售位###
    find_but = soup.xpath('//*[@id="listDataGO"]//div/div//div[10]//span[2]')
    for g in find_but:
        find_but_list.append(g.text)
dataframe1 = pd.DataFrame({'出發日期': go_date_list, '行程名稱': title_list, '旅遊天數': find_play_day_list, '價錢': find_pay_list
                              , '總團位': find_total_list, '可售位': find_but_list})
dataframe1.to_excel('C:\專案\\4p.xlsx', index=False)
for p in range(len(go_date_list)):
    go_da = go_date_list[p]
    title_l = title_list[p]
    find_p = find_play_day_list[p]
    pri = find_pay_list[p]
    find_total_l = find_total_list[p]
    url_l = find_but_list[p]
    country = '1'
    company = '2'
    try:
        cursor.execute('INSERT INTO all_data (date, title, trip_date, price, all_set, sale_set, country, company) VALUES (%s,%s,%s,%s,%s,%s,%s,%s);', (go_da, title_l, find_p, pri, find_total_l, url_l, country, company))
        conn.commit()
    except:
        pass
conn.close()