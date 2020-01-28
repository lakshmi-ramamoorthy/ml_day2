# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 01:51:47 2020

@author: RPS
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('MSFT.csv')
df=pd.DataFrame({"Open" : df["Open"],"Close":df["Close"]})
print(df)

x=np.array(df["Open"]).reshape(-1,1)
y=np.array(df["Close"]).reshape(-1,1)
from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(x,y)
print("predict" ,model.predict([[87]]))

MSE=np.mean((87-model.predict([[87 ]]))**2)
print("Mean square error %r" %(MSE))
