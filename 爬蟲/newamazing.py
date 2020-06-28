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
url_list = []
for f in range(1, 6):
    url = 'https://www.newamazing.com.tw/EW/GO/GroupList.asp?pageGO='+str(f)+'&tabList=GO&regmCd=0001'
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
    find_url = soup.xpath('//*[@id="listDataGO"]//div/div//div[3]/a/@href')
    new_urls = []
    for k in find_url:
       new_url = 'https://www.newamazing.com.tw/'+k
       new_urls.append(new_url)
    count_new_urls = len(new_urls)
    for h in range(count_new_urls):
        url1 = new_urls[h]
        html1 = requests.get(url1)
        soup1 = etree.HTML(html1.text)
        find_but = soup1.xpath('//*[@id="Main"]/div//div//ul[1]//li//a/span')
        for g in find_but:
            url_list.append(g.text)
#  ###可售位###


dataframe1 = pd.DataFrame({'出發日期': go_date_list, '行程名稱': title_list, '旅遊天數': find_play_day_list, '價錢': find_pay_list
                              , '總團位': find_total_list, '可售位': url_list})
dataframe1.to_excel('C:\專案\\newamazing.xlsx', index=False)
for p in range(len(go_date_list)): 
    go_da = go_date_list[p]
    title_l = title_list[p]
    find_p = find_play_day_list[p]
    pri = find_pay_list[p]
    find_total_l = find_total_list[p]
    url_l = url_list[p]
    country = '1'
    company = '1'
    try:
        cursor.execute('INSERT INTO all_data (date, title, trip_date, price, all_set, sale_set, country, company) VALUES (%s,%s,%s,%s,%s,%s,%s,%s);', (go_da, title_l, find_p, pri, find_total_l, url_l, country, company))
        conn.commit()
    except:
        pass
conn.close()
