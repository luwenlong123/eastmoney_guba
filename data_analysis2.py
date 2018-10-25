# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 14:39:18 2018

@author: dell
"""

import pandas as pd

data = pd.read_excel('000831.xlsx')
data = data.reset_index(drop=True)

import tushare as ts
hq_df = ts.get_hist_data('000831')

data['years'] = 2018
data['fz'] = '-'

data.years[8896:47945] = 2017
data.years = data.years.astype('str')
data['date'] = data['years'] + data['fz'] + data['pubtime']
data2 = data.iloc[0:10606,:]
data3 = data2.iloc[:,[0,1,2,3,10]]

s = data3.groupby(by='date')
df1 = s.count()
df2 = s.sum()
df2.columns=['read_sum','dis_sum']
all_df = hq_df.join(df1)
all_df = all_df.join(df2)