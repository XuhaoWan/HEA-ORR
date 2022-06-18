#!/usr/bin/env python
# -*- coding:utf-8 -*-
#author: xhwan

import numpy as np


sites_type = np.load('pretype.npy')


for i in range(0, 12000):
    if sites_type[i] == 'FeRu':
        sites_type[i] = 'RuFe'
    elif sites_type[i] == 'FeRh':
        sites_type[i] = 'RhFe'
    elif sites_type[i] == 'RhRu':
        sites_type[i] = 'RuRh'
    elif sites_type[i] == 'FeIr':
        sites_type[i] = 'IrFe'
    elif sites_type[i] == 'RuIr':
        sites_type[i] = 'IrRu'
    elif sites_type[i] == 'RhIr':
        sites_type[i] = 'IrRh'
    elif sites_type[i] == 'RuPt':
        sites_type[i] = 'PtRu'
    elif sites_type[i] == 'FePt':
        sites_type[i] = 'PtFe'
    elif sites_type[i] == 'RhPt':
        sites_type[i] = 'PtRh'
    elif sites_type[i] == 'AgRu':
        sites_type[i] = 'RuAg'
    elif sites_type[i] == 'PtIr':
        sites_type[i] = 'IrPt'
    elif sites_type[i] == 'FeAg':
        sites_type[i] = 'AgFe'
    elif sites_type[i] == 'AgPt':
        sites_type[i] = 'PtAg'
    elif sites_type[i] == 'AgRh':
        sites_type[i] = 'RhAg'
    elif sites_type[i] == 'AgIr':
        sites_type[i] = 'IrAg'
    else:
        pass


with open('pretype', 'a') as fout:
    for line in sites_type:
        line_new = line + ','+'\n'
        fout.write(line_new)