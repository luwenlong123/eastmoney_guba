# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 21:27:26 2018

@author: dell
"""

import requests

url = 'http://guba.eastmoney.com/list,600006,f.html'
html = requests.get(url)


url = 'http://guba.eastmoney.com/remenba.aspx?type=1&tab=1'
html = requests.get(url)
from lxml import etree
et = etree.HTML(html.text)

gp_list = []

for i in range(1,61):
    gp_list.append(et.xpath('/html/body/div[1]/div[5]/div[2]/div[1]/div/ul[1]/li['+str(i)+']/a')[0].text)

for i in range(1,1433):
    gp_list.append(et.xpath('/html/body/div[1]/div[5]/div[2]/div[1]/div/ul[2]/li['+str(i)+']/a')[0].text)
    
url = 'http://guba.eastmoney.com/remenba.aspx?type=1&tab=2'
html = requests.get(url)
from lxml import etree
et = etree.HTML(html.text)

for i in range(1,61):
    gp_list.append(et.xpath('/html/body/div[1]/div[5]/div[2]/div[1]/div/ul[1]/li['+str(i)+']/a')[0].text)

for i in range(1,2116):
    gp_list.append(et.xpath('/html/body/div[1]/div[5]/div[2]/div[1]/div/ul[2]/li['+str(i)+']/a')[0].text)
    
dm_list = []
name_list = []
for i in gp_list:
    dm_list.append(i.split('(')[1].split(')')[0])
    name_list.append(i.split('(')[1].split(')')[1])
    

all_html = []
newdm_list = []
def get_gbpl(i):
    url = 'http://guba.eastmoney.com/list,'+i+',f.html'
    html = requests.get(url)
    newdm_list.append(i)
    all_html.append(html)

    
import threading
thread_list = []
for i in dm_list:
    thread_list.append(threading.Thread(target=get_gbpl, args=(i,)))
    
for t in thread_list:
    t.start()



#test_get_new




    