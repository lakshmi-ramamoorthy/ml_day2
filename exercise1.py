# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 20:27:35 2020

@author: RPS
"""

import pandas as pd
import numpy as np

"""
dataset=pd.read_csv("Data.csv")
print(dataset.shape)

x=dataset.iloc[:,:-1].values
y=dataset.iloc[:,3].values
print(x)
print(y)
print(dataset.head())

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan,strategy='mean')

x[:,1:3] = imputer.fit_transform(x[:,3])
print(x[:,2])
print(x[:,0])
"""
"""
dataset=pd.read_csv("BlackFriday.csv")
print(dataset.shape)
x=dataset.iloc[:,:].values
print(x)

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan,strategy='mean')

x[:,10:11] = imputer.fit_transform(x[:,10:11])
print(x)
"""

from sklearn.preprocessing import LabelEncoder
dataset=pd.read_csv("Data.csv")
print(dataset.shape)

X=dataset.iloc[:,:-1].values

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan,strategy='mean')

X[:,1:3] = imputer.fit_transform(X[:,1:3])
y=dataset.iloc[:,3].values

labelEnc_X = LabelEncoder()
X[:,0] = labelEnc_X.fit_transform(X[:,0])
print(X)

print(labelEnc_X.fit_transform(y))


