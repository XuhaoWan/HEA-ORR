#!/usr/bin/env python
# -*- coding:utf-8 -*-
#author: xhwan

import linecache
import random

HEA_Id = input('Please input HEA ID:')
lat_con = input('Please input lattice constant:')
HEAele = input('Please input elements of HEA:')
eleno = input('Please input numbers of elements:')

filename = 'POSCAR.BCC'
outname = 'HEA'+ HEA_Id + '.vasp'

lines = []

lat_con = float(lat_con)
strain = str(lat_con/3.919)

for i in range(1, 10):
    text = linecache.getline(filename, i)
    lines.append(text)

lines[0] = outname + '\n'
lines[1] = strain + '\n'
lines[5] = HEAele + '\n'
lines[6] = eleno + '\n'

with open(outname, 'w') as fout:
    for line in lines:
        fout.write(line)

del lines[:]

for i in range(10, 42):
    text = linecache.getline(filename, i)
    lines.append(text)

random.shuffle(lines)

with open(outname, 'a') as fout:
    for line in lines:
        fout.write(line)


