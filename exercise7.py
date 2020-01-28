# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 03:05:12 2020

@author: RPS
"""

import numpy as np
import pandas as pd
import sklearn

dataset=pd.read_csv('MSFT.csv')
X= dataset.iloc[:,1:4].values
Y=dataset.iloc[:,5].values
print(X)
print(Y)



from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.3,random_state=0)

print(X_test)
print(Y_test)

model = LinearRegression()
model.fit(X_test, Y_test)
predictions = model.predict(X_test)
for i, prediction in enumerate(predictions):
    print ('Predicted: %s, Target: %s' % (prediction, Y_test[i]))
    print ('R-squared: %.2f' % model.score(X_test, Y_test))

import statsmodels.api as sm

est = sm.OLS(Y_test,X_test) #ordinary least square method 
est2 = est.fit()
print("Summary.....")
print(est2.summary())
