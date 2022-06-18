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



dataset_label = np.loadtxt('dataset_label.csv', delimiter=",", dtype="float")
dataset = np.loadtxt('datasetk.csv',  delimiter=',', dtype="float")


x = dataset

ss = MinMaxScaler()
x = ss.fit_transform(x)
y = dataset_label

params = {'n_estimators': 500,
          'max_depth': 5,
          'min_samples_split': 5,
          'learning_rate': 0.01,
          'loss': 'huber'}

model = GBR(**params)
model.fit(x, y)


FI = model.feature_importances_

FI_atoms = []
FI_features = []

for i in range(15):
    Fiatoms = FI[6*i+0] + FI[6*i+1]+ FI[6*i+2]+ FI[6*i+3]+ FI[6*i+4]+ FI[6*i+5]
    FI_atoms.append(Fiatoms)


for j  in range(6):
    Fifeature = 0
    for p in range(15):
        Fifeature = Fifeature + FI[p*6+j]
    FI_features.append(Fifeature)


print(FI_atoms)
print(FI_features)