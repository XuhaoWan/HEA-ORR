#!/usr/bin/env python
# -*- coding:utf-8 -*-
#author: xhwan

import math


class HEA:
    def __init__(self, name, number, energy):
        self.name = name
        self.number = number
        self.energy = energy


class einHEA:
    def __init__(self, name, number, energy):
        self.name = name
        self.number = number
        self.energy = energy


Ir = einHEA('Ir', 6, -9.512754716)
Pt = einHEA('Pt', 6, -6.846261091)
Ru = einHEA('Ru', 6, -3.321467062)
Rh = einHEA('Rh', 7, -7.711290544)
Fe = einHEA('Fe', 7, -7.322064543)
Ag = einHEA('Ag', 0, -9.441455317)

IrPtRuRhAg = HEA('IrPtRuRhAg', 66776, -8.745078636 )

Epureall = Ir.number*float(Ir.energy)+Pt.number*float(Pt.energy)+Rh.number*float(Rh.energy) +
           Ru.number*float(Ru.energy)+Ag.number*float(Ag.energy)+Fe.number*float(Fe.energy)
Epure = Epureall/32

dH = IrPtRuRhAg.energy - Epure
TM = 2287.06


a = math.log(7/32)
b = 14*a/32
c = math.log(6/32)
d = 18*c/32
ka = b + d

dS = -ka * (8.314*6.0221415/16021.77)

sigma = TM*dS/abs(dH)

print(dS)
print(dH)
print(sigma)
