#!/usr/bin/env python
# -*- coding:utf-8 -*-
#author: xhwan

import math

R_ave = 169.8

class einHEA:
    def __init__(self, name, number, radius):
        self.name = name
        self.number = number
        self.radius = radius



Pt = einHEA('Pt', 6, 177)
Ru = einHEA('Ru', 6, 178)
Rh = einHEA('Rh', 6, 173)
Ag = einHEA('Ag', 7, 165)
Fe = einHEA('Fe', 7, 156)
Ir = einHEA('Ir', 0, 180)

N = Ir.number*math.pow((1-Ir.radius/R_ave), 2) + Pt.number*math.pow((1-Pt.radius/R_ave), 2) + \
    Ru.number*math.pow((1-Ru.radius/R_ave), 2) + Rh.number*math.pow((1-Rh.radius/R_ave), 2) + \
    Ag.number*math.pow((1-Ag.radius/R_ave), 2) + Fe.number*math.pow((1-Fe.radius/R_ave), 2)
N_d = N/32

delta = math.sqrt(N_d)

print(delta)