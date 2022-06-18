#!/usr/bin/env python
# -*- coding:utf-8 -*-
#author: xhwan
import ase.build
from ase.io import read, write
from ase.visualize import view
from ase import Atoms
import numpy as np


HEA = input('HEA_name:')
model = read(str(HEA+'.vasp'))


coord = np.array([[0, 0, 0], [0, 0, 0.95]]) # OH bondlength


for i in range(10000):
    outstru = 'F:\\HEA\\code\\enhance\\a\\'+ str(i)+'.vasp'
    
    atom_pos = model.get_positions()
    np.random.shuffle(atom_pos)
    model.set_positions(atom_pos)
    
    slab_111 = ase.build.surface(model, (1, 1, 1), layers=2, vacuum=10)
    slab_111.rotate(180, 'x', rotate_cell = True)

    slab_111.extend(Atoms('OH', coord + np.array([6.243, -3.6045, -8.243])))
    
    #write('surf.png', slab_111)
    view(slab_111)
    write(outstru, slab_111, format='vasp')