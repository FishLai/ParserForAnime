# coding=utf-8
'''
Created on 2018/8/20

@author: quan_
'''
from lxml import etree, html
from lxml.html import html5parser as h5p
import requests
import requests_html as req_h
import json

base_link = "https://share.dmhy.org" #home page
params_dict = {}
def initialParameter():
    #start scrape
    link = base_link
    session = req_h.HTMLSession()
    response = session.get(link)
    #execute javascript
    response.html.render()
    #start scrape days parameter
    days = response.html.find('#mini_jmd > table.jmd_base > tbody > tr > th')
    ls_days = []
    for day in days:
        ls_days.append(day.text)
    
    
    #scrape out animes
    node_days = response.html.find('#mini_jmd > table.jmd_base > tbody > tr > td')
    ls_animes = []
    for node_day in node_days:
        index = node_days.index(node_day)
        anInDay = node_day.find('a') #animes in one day
        ls_animes.append([])
        for anime in anInDay:
            ls_animes[index].append(anime.text)
    
    dict_day_animes = {}
    for day in ls_days:
        index = ls_days.index(day)
        dict_day_animes[day] = ls_animes[index]
    
    f = open('somePara.json', 'w', encoding='utf-8')
    j_params = json.dumps(dict_day_animes, ensure_ascii=False)
    f.write(j_params)
    f.close()
    
    

def parseSeasonUpdate():
    link = "https://share.dmhy.org" #url of homepage
    session = req_h.HTMLSession()
    response = session.get(link)
    response.html.render()
    days = response.html.find('#mini_jmd > table.jmd_base > tbody > tr > th')
    for day in days:
        print(day.text)
    
    #tree = h5p.(link)
    '''
    node_be = '//div[@id="mini_jmd"]/*[@class="jmd"]' #node_be, node_begining means I appoint a node in the lxml tree
    node_th = node_be + "" #which point days 
    print (node_th)
    days = tree.xpath(node_be) #node_w, days place
    print(days)
    '''
    '''
    rows = iter(table)
    headers = [col.text for col in next(rows)]
    for row in rows:
        values = [col.text for col in row]
        print(dict(zip(headers, values)))
    '''
    
def parseWeekUpdate():
    link = "https://share.dmhy.org/topics/list?keyword=OVERLORD"
    response = requests.get(link)
    tree = html.fromstring(response.text)

    nodes = '//table[@id="topic_list"]//a[@target="_blank"]/text()'
    titles = tree.xpath(nodes)
    print(titles, '\n',len(titles))\
    
if __name__ == '__main__':
    import time
    start_time = time.time()
    initialParameter()
    print(time.time() - start_time)