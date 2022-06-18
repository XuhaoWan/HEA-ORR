#!/usr/bin/env python
# -*- coding:utf-8 -*-
#author: xhwan

import ase.build
from ase.io import read, write
from ase.visualize import view
from ase import Atoms
import numpy as np
from ase import neighborlist


model = read('x.vasp')


syminfo = model.get_chemical_symbols()
for i in range(len(model)):
    if syminfo[i]== 'O':
        I_O = i
    elif syminfo[i]== 'H':
        I_H = i
    else:
        pass
        
pos_O = model[I_O].position
pos_O[2] = -8.197
pos_H = model[I_H].position
pos_H[2] = -8.197 + 0.95

model[I_O].position = pos_O
model[I_H].position = pos_H

write('x.vasp', model, format='vasp')