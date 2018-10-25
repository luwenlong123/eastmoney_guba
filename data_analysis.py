# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 20:41:24 2018

@author: dell
"""

#import pandas as pd
#
#data = pd.read_excel('000831.xlsx')

data = data.reset_index(drop=True)

from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
vectorizer = CountVectorizer(input='content',
                             encoding='utf-8',
                             decode_error='strict',
                             strip_accents=None,
                             lowercase=True,
                             preprocessor=None,
                             tokenizer=None,
                             stop_words=None,
                             token_pattern='(?u)\\b\\w\\w+\\b',
                             ngram_range=(1, 1),
                             analyzer='word',
                             max_df=1.0,
                             min_df=1,
                             max_features=None,
                             vocabulary=None,
                             binary=False,)
                             #dtype=<class 'numpy.int64'>)


Tf = TfidfVectorizer(input='content',
                     encoding='utf-8', 
                     decode_error='strict',
                     strip_accents=None, 
                     lowercase=True, 
                     preprocessor=None,
                     tokenizer=None,
                     analyzer='word',
                     stop_words=None,
                     token_pattern='(?u)\\b\\w\\w+\\b',
                     ngram_range=(1, 1),
                     max_df=1.0,
                     min_df=1,
                     max_features=None,
                     vocabulary=None,
                     binary=False,)
                     #dtype=<class 'numpy.float64'>, 
                     #norm='l2', 
                     #use_idf=True,
                     #smooth_idf=True,
                     #sublinear_tf=False)

#v = vectorizer.fit_transform(list(data.title)[0:100])
#t = Tf.fit_transform(list(data.title)[0:100])
#
#v = vectorizer.fit_transform(list(data.title_word[0:100]))
#t = Tf.fit_transform(data.title_word[0])



#print(vectorizer.get_feature_names())
#a = v.toarray()
#b = t.toarray()


import jieba
s = jieba.cut(data.title[0])
sl1 = list(s)
sl = jieba.lcut(data.title[0])
sa = jieba.lcut(list(data.title[0:100]))

def get_word(w_g):
    s = str()
    for i in w_g:
        s = s+' '+ i
    return s


fc = []
for i in range(len(data.title)):
    try:
        fc.append(get_word(jieba.lcut(data.title[i])))
        print(i)
    except AttributeError as e:
        fc.append(str(data.title[i]))

data['title_word'] = fc

v = vectorizer.fit_transform(list(data.title_word[0:155470]))
#t = Tf.fit_transform(data.title_word[0])

print(vectorizer.get_feature_names())
a = v.toarray()

############################################################
#获取行情数据
import tushare as ts
hq_df = ts.get_hist_data('000831')
#pro = ts.pro_api()
#
#df = pro.daily(ts_code='000831.SZ', start_date='20000701', end_date='20180718')











