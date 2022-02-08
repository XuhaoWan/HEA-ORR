#!/usr/bin/env python
# -*- coding:utf-8 -*-
#author: xhwan

import ase.build
from ase.io import read, write
from ase.visualize import view
from ase import Atoms

if miller_index == 100:
    CN = 8
    noc = 14
import numpy as np
from ase import neighborlist

miller_index = 100
noc = 0
elif miller_index == 111:
    CN = 9
    noc = 15
else:
    pass


def get_coord_atoms(fname, noc):
    model = read(fname)
    syminfo = model.get_chemical_symbols()
    for i in range(len(model)):
        if syminfo[i]== 'O':
            I_O = i
        elif syminfo[i]== 'H':
            I_H = i
        else:
            pass
    #print(model[I_H],model[I_O])
    HEA_index = list(range(len(model)))
    HEA_index.remove(I_H)
    HEA_index.remove(I_O)
    dmat = model.get_distances(I_O, HEA_index)
    np_dmat = np.array(dmat)
    srtindex = np_dmat.argsort()
    nb_sym = []
    nb_dis = []
    for i in range(noc):
        j = srtindex[i]
        nb_sym.append(model[j].symbol)
        nb_dis.append(dmat[j])
    return nb_sym, nb_dis



def get_surfinf(sym, dis,  coord_num):
    Ir = [180, 2.20, 7, -2.25]
    Pt = [177, 2.28, 9, -2.42]
    Ru = [178, 2.20, 7, -1.95]
    Rh = [173, 2.28, 8, -2.18]
    Ag = [165, 1.93, 10, -4.04]
    Fe = [156, 1.83, 6, -0.81]
    data = np.zeros(shape = (15, 6))
    for i in range(len(sym)):
        if sym[i] == 'Ir':
            dataIr = Ir.copy()
            dataIr.append(coord_num)
            dataIr.append(dis[i])
            #print(dataIr)
            data[i, :] = dataIr
        elif sym[i] == 'Pt':
            dataPt = Pt.copy()
            dataPt.append(coord_num)
            dataPt.append(dis[i])
            #print(dataPt)
            data[i, :] = dataPt
        elif sym[i] == 'Ru':
            dataRu = Ru.copy()
            dataRu.append(coord_num)
            dataRu.append(dis[i])
            # print(dataRu)
            data[i, :] = dataRu
        elif sym[i] == 'Rh':
            dataRh = Rh.copy()
            dataRh.append(coord_num)
            dataRh.append(dis[i])
            # print(dataRh)
            data[i, :] = dataRh
        elif sym[i] == 'Ag':
            dataAg = Ag.copy()
            dataAg.append(coord_num)
            dataAg.append(dis[i])
            # print(dataAg)
            data[i, :] = dataAg
        elif sym[i] == 'Fe':
            dataFe = Fe.copy()
            dataFe.append(coord_num)
            dataFe.append(dis[i])
            #print(dataFe)
            data[i, :] = dataFe
        else:
            print('Error! Unknown element')
    return data



AS_num = 180
dataset = np.zeros(shape = (AS_num, 15, 6))
for j in range(AS_num):

    fname = str(j+1)+'.vasp'
    symbols, distances = get_coord_atoms(fname, noc)
    print(symbols, distances)
    data_single = get_surfinf(symbols, distances, CN)
    dataset[j : ] = data_single


