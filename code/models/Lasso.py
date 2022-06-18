#!/usr/bin/env python
# -*- coding:utf-8 -*-
#author: xhwan

import numpy as np
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler


dataset_label = np.loadtxt('dataset_label.csv', delimiter=",", dtype="float")


dataset = np.loadtxt('dataset.csv',  delimiter=',', dtype="float")


x = dataset

ss = MinMaxScaler()
x = ss.fit_transform(x)
y = dataset_label

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=90)


params = {'alpha': 0.5 ,
          'fit_intercept': True,
          'normalize': False,
          'precompute': False,
          'max_iter': 1000,
          'tol': 1e-4,
          'warm_start': False,
          'positive': False,
          'selection': 'cyclic',
          'random_state': 8}

model = Lasso(**params)
model.fit(x_train,y_train)

rmse = np.sqrt(mse(y_train,model.predict(x_train)))
r2 = r2_score(y_train,model.predict(x_train))
rmset = np.sqrt(mse(y_test,model.predict(x_test)))
r2t = r2_score(y_test,model.predict(x_test))


print('pre:', model.predict(x_test))
print(y_test)
print('RMSE:', rmse)
print('R2:', r2)
print('RMSEt:', rmset)
print('R2t:', r2t)

