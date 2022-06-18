#!/usr/bin/env python
# -*- coding:utf-8 -*-
#author: xhwan

from ase.data import covalent_radii
import numpy as np
from ase.io import read, write
from ase import Atoms
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt


bulk = read('egmodel.vasp')
surf = read('egmodel.vasp')


def get_surfAtom_byXY(atoms, xypos, scale=2):
    radiiAll = scale * np.array([covalent_radii[i] for i in atoms.get_atomic_numbers()])
    z_test = max(atoms.get_positions()[:, 2])+5
    surfIndex = []
    while len(surfIndex) == 0:
        testAtom = Atoms(['H'], [[xypos[0], xypos[1], z_test]])
        tmpAtoms = atoms.copy()
        tmpAtoms.extend(testAtom)
        dist_test = list(tmpAtoms.get_distances(-1, list(range(len(atoms)))) - radiiAll)
        for i in dist_test:
            if i < 0:
                surfIndex.append(dist_test.index(i))
        z_test -= 0.1
    return surfIndex

def get_surf_grid(atoms, mesh=10):
    cell = atoms.get_cell()
    grids = np.linspace(0, 1, mesh, endpoint=False)
    surfList = []
    for i in grids:
        for j in grids:
            surfList += get_surfAtom_byXY(atoms, [cell[0][0]*i+cell[1][0]*j, cell[0][1]*i+cell[1][1]*j] )
    return sorted(list(set(surfList)))

def get_extended_atoms(atoms):
    tmpAtoms = atoms.copy()
    tmpAtoms = atoms*[3,3,1]
    tmpAtoms.set_positions(tmpAtoms.get_positions() -atoms.get_cell()[0]-atoms.get_cell()[1])
    return tmpAtoms


surfList = get_surf_grid(bulk)

del surf[[i for i in range(len(surf)) if i not in surfList]]

surf_ext = get_extended_atoms(surf)

atop = surf.get_positions()
pos_ext = surf.get_positions()
tri = Delaunay(pos_ext[:, : 2])
pos_nodes = pos_ext[tri.simplices]

hollow = np.array([t.sum(axis=0)/3 for t in pos_nodes])

bridge = []
for i in pos_nodes:
    bridge.append((i[0]+i[1])/2)
    bridge.append((i[0]+i[2])/2)
    bridge.append((i[1]+i[2])/2)
bridge = np.array(bridge)


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.triplot(pos_ext[:, 0], pos_ext[:, 1], triangles=tri.vertices, color='grey')
ax.plot(hollow[:, 0],  hollow[:, 1],  'ok', label='Hollow')
ax.plot(bridge[:, 0],  bridge[:, 1],  'or', label='Bridge')
ax.plot(pos_ext[:, 0], pos_ext[:, 1], 'ob', label='Atop')
#plt.legend(loc='lower left')
plt.axis('scaled')
plt.axis('off')


cell_param = surf.get_cell()
ax.set_xlim([cell_param[1][0]-0.2, cell_param[0][0]])
ax.set_ylim([cell_param[0][1]-0.2, cell_param[1][1]])
plt.xticks([])
plt.yticks([])


plt.savefig('ads.png',  bbox_inches = "tight", transparent=True)

#write('surf.png', bulk)

