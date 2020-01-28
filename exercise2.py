# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 22:43:51 2020

@author: RPS
"""

import pandas as pd


dataset=pd.read_json("http://restcountries.eu/rest/v2/all")
print(dataset['name'])

from sklearn.preprocessing import LabelEncoder
labelEnc_X= LabelEncoder()
dataset['name']=labelEnc_X.fit_transform(dataset['name'])
print(dataset['name'])
