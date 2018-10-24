# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 10:26:54 2018

@author: dell
"""

import em_get
import pandas as pd

all_data = pd.DataFrame()
for i in range(1,1945):
    gm_pl = em_get.get_guba(code='000831',page=i)
    all_data = pd.concat((all_data,gm_pl))
    print(i)

