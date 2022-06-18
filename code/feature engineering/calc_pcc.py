#!/usr/bin/env python
# -*- coding:utf-8 -*-
#author: xhwan

from scipy.stats import pearsonr
import pandas as pd
import numpy as np
from sklearn import preprocessing



min_max_scaler = preprocessing.MinMaxScaler()


df = pd.read_csv('feature.csv', index_col=0)


df = np.array(df.values)
df = min_max_scaler.fit_transform(df)


var = df.var(axis = 0)
print(var)


pccs = np.corrcoef(df, rowvar=0)
np.savetxt('atomicfeature.csv', pccs)

