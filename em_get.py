# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 21:31:47 2018

@author: luwenlong321
"""

import requests
from lxml import etree
from bs4 import BeautifulSoup
import pandas as pd

###########################################################################
#定义函数get_guba，获取指定股票指定页数的评论
#由于股票代码会00开头，因此该函数需要接收字符串的股票代码输入
def get_guba(code='600000',page=1):
    url = 'http://guba.eastmoney.com/list,' + code +  ',f_' +str(page)+ '.html'
    html = requests.get(url)
    bs = BeautifulSoup(html.text)
    art = bs.select('#articlelistnew')[0]
    divs = art.findAll('div')
    read_list = []
    dis_list = []
    title_list = []
    author_list = []
    pubtime_list = []
    updatetime_list = []
    page_list = []
    code_list = []
#由于网页结构的原因，要设置个分支    
    for i in range(1,len(art.findAll('div'))-2):
        if len(divs[i].findAll('span')) == 6:
            try:
                read_list.append(divs[i].findAll('span')[0].text)
            except Exception as e:
                read_list.append(' ')
            try:
                dis_list.append(divs[i].findAll('span')[1].text)
            except Exception as e:
                dis_list.append(' ')
            try:
                title_list.append(divs[i].findAll('span')[2].findAll('a')[0]['title'])
            except Exception as e:
                title_list.append(' ')
            try:
                author_list.append(divs[i].findAll('span')[3].text)
            except Exception as e:
                author_list.append(' ')
            try:
                pubtime_list.append(divs[i].findAll('span')[4].text)
            except Exception as e:
                pubtime_list.append(' ')
            try:
                updatetime_list.append(divs[i].findAll('span')[5].text)
            except Exception as e:
                updatetime_list.append(' ')    
            page_list.append(page)
            code_list.append(code)
        if len(divs[i].findAll('span')) == 7:
            try:
                read_list.append(divs[i].findAll('span')[0].text)
            except Exception as e:
                read_list.append(' ')
            try:
                dis_list.append(divs[i].findAll('span')[1].text)
            except Exception as e:
                dis_list.append(' ')
            try:
                title_list.append(divs[i].findAll('span')[2].findAll('a')[0]['title'])
            except Exception as e:
                title_list.append(' ')
            try:
                author_list.append(divs[i].findAll('span')[4].text)
            except Exception as e:
                author_list.append(' ')
            try:
                pubtime_list.append(divs[i].findAll('span')[5].text)
            except Exception as e:
                pubtime_list.append(' ')
            try:
                updatetime_list.append(divs[i].findAll('span')[6].text)
            except Exception as e:
                updatetime_list.append(' ')       
            page_list.append(page)
            code_list.append(code)
    data = pd.DataFrame()
    data['readed'] = read_list
    data['dis'] = dis_list
    data['title'] = title_list
    data['author'] = author_list
    data['pubtime'] = pubtime_list
    data['updatetime'] = updatetime_list
    data['page'] = page_list
    data['code_list'] = code_list
    return data

####################################################################
#获取所有股票的名称及代码,返回DataFrame格式
def get_all_stockcode():
    code_list = []
    url = 'http://guba.eastmoney.com/remenba.aspx?type=1&tab=1'
    html = requests.get(url)    
    bs = BeautifulSoup(html.text)
    bs.findAll(name='div',class_='ngbglistdiv')
    shcode_list = bs.findAll(name='div',class_='ngbglistdiv')[0].findAll('li')
    for i in shcode_list:
        code_list.append(i.text)
    url = 'http://guba.eastmoney.com/remenba.aspx?type=1&tab=2'
    html = requests.get(url)    
    bs = BeautifulSoup(html.text)
    bs.findAll(name='div',class_='ngbglistdiv')
    shcode_list = bs.findAll(name='div',class_='ngbglistdiv')[0].findAll('li')
    for i in shcode_list:
        code_list.append(i.text)
    code_df = pd.DataFrame()
    code_df['code'] = code_list
    return code_df
    
######################################################################
#在不模拟浏览器的情况下获取对应股票的最大页数    
url = 'http://guba.eastmoney.com/list,600000,f_3809.html'
html = requests.get(url)



    
    
    
    