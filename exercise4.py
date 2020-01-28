# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 01:02:50 2020

@author: RPS
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x=[[6],[8],[10],[14],[18]]
print(x[0])
y=[[7],[9],[13],[15],[18]]

plt.figure()
plt.title("Plotting...")
plt.xlabel("Pizza Diameter")
plt.ylabel("Pizza cost")
plt.plot(x,y)
plt.grid(True)
plt.show()

from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(x,y)
print("predict" ,model.predict([[14]]))

MSE=np.mean((15-model.predict([[14]]))**2)
print("Mean square error %r" %(MSE))



