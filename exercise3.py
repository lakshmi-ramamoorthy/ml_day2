# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 23:01:57 2020

@author: RPS
"""
import pandas as pd
#dataset=pd.read_csv("BlackFriday.csv")
#print(dataset.groupby('Age').count())

"""
print(dataset.shape)

X=dataset.iloc[:,:-1].values
y=dataset.iloc[:,11].values

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,y,test_size=0.3,random_state=0)

print(X_train.size)
print(X_test.size)
"""
"""
# Age vector
age = (25, 35, 50)
# Salary vector
salary = (200000, 1200000, 2000000)
# Data frame created using age and salary
df = pd.DataFrame( {"Age":age, "Salary":salary})
print(df)

from sklearn import preprocessing
x = df.values #returns a numpy array
print(x)
min_max_scaler = preprocessing.MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(x)
df = pd.DataFrame(x_scaled)
print(df)
"""

df=pd.read_csv("C:/Users/RPS/Desktop/Training/day2/population.csv")
print(df['Year'],df['Value'])


df=pd.DataFrame( {"Year":df["Year"], "Population":df["Value"]})
print(df)

from sklearn import preprocessing
min_max_scaler = preprocessing.MinMaxScaler()
x=df.values
#y=df['Value'].values
x_scaled = min_max_scaler.fit_transform(x)
#y_scaled = min_max_scaler.fit_transform(y)
df = pd.DataFrame(x_scaled)
print(df)
