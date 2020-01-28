# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 01:25:17 2020

@author: RPS
"""

#read data
#check data is clean 
#Encoding
#Scaling
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('Salary_Data.csv')
df=pd.DataFrame({"Years" : df["YearsExperience"],"Salary":df["Salary"]})
print(df)
"""
from sklearn import preprocessing
min_max_scaler = preprocessing.MinMaxScaler()
x=df.values
print(x)
#y=df['Value'].values
x_scaled = min_max_scaler.fit_transform(x)
#y_scaled = min_max_scaler.fit_transform(y)
df = pd.DataFrame(x_scaled)
print(df)
"""
Xaxis=df.iloc[:,:-1]
print(Xaxis)

Yaxis=df.iloc[:,1].values
print(Yaxis)

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(Xaxis,Yaxis,test_size=0.3,random_state=0)

print(X_train)
print(Y_train)

plt.figure()
plt.title("Plotting...")
plt.xlabel("Pizza Diameter")
plt.ylabel("Pizza cost")
plt.plot(X_train,Y_train)
plt.grid(True)
plt.show()

"""
from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(X_train,Y_train)
print("predict" ,model.predict([[10]]))
"""


x=np.array(df["Years"]).reshape(-1,1)
y=np.array(df["Salary"]).reshape(-1,1)
from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(x,y)
print("predict" ,model.predict([[10]]))








