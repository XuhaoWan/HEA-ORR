#!/usr/bin/env python
# -*- coding:utf-8 -*-
#author: xhwan

import numpy as np
from sklearn.ensemble import GradientBoostingRegressor as GBR
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn import preprocessing
from sklearn.externals import joblib

model = joblib.load('GBR.pkl')


data_pre = np.load('data.npy')
data_pre = data_pre.reshape(12000, 90)



x_pre = data_pre

ss = MinMaxScaler()
x_pre = ss.fit_transform(x_pre_)



y_pre = model.predict(x_pre)
np.savetxt('pre_value.csv', y_pre, delimiter=',')

