#!/usr/bin/env python
# -*- coding:utf-8 -*-
#author: xhwan
import ase.build
from ase.io import read, write
from ase.visualize import view
from ase import Atoms
import numpy as np


surf_type = 100
coord = np.array([[0, 0, 0], [0, 0, 0.95]]) # OH bondlength

if surf_type == 100:
    for q in range(6):
        for i in range(10):
            fname = 'HEA'+str(i+1+q*10)+'.vasp'
            model = read(fname)
            for j in range(100):
                atom_pos = model.get_positions()
                np.random.shuffle(atom_pos)
                model.set_positions(atom_pos)
            
                outstru = str(q*1000+100*i+j+1)+'.vasp'
                
                slab_100 = ase.build.surface(model, (1, 0, 0),  layers=1, vacuum = 10)

                slab_100.extend(Atoms('OH', coord + np.array([2.943, 2.943, 17.686])))
            
                write(outstru, slab_100, format='png')
                write(outstru, slab_100, format='vasp')
                view(slab_100)
elif surf_type == 111:                    
    for q in range(6):
        for i in range(10):
            fname = 'HEA'+str(i+1+q*10)+'.vasp'
            model = read(fname)
            for j in range(100):
                atom_pos = model.get_positions()
                np.random.shuffle(atom_pos)
                model.set_positions(atom_pos)
            
                outstru = str(6000+q*1000+100*i+j+1)+'.vasp'
                
                slab_111 = ase.build.surface(model, (1, 1, 1),  layers=2, vacuum = 10)
                slab_111.rotate(180, 'x', rotate_cell = True)

                slab_111.extend(Atoms('OH', coord + np.array([2.943, 2.943, 17.686])))
            
                write(outstru, slab_100, format='png')
                write(outstru, slab_100, format='vasp')
                view(slab_100)
else:
    print('Surface type error')