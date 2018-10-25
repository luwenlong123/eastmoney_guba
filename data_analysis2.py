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