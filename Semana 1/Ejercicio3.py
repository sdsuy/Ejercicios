# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 11:53:28 2020

@author: Santiago
"""

h = input('Ingrese las horas ')
m = input('Ingrese los minutos ')
s = input('Ingrese los segundos ')

s = int(s)
m = int(m)
h = int(h)

s += (h * 60 + m) * 60

print('La cantidad total de segundos es ' + str(s))
