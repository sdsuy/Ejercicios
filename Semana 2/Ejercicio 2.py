# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 16:25:04 2020

@author: Santiago
"""

file = open('numeros.txt', 'r')
lista = file.read()
lista = lista.split()
lista = list(map(int, lista))
print('El mayor entero ingresado es: ' + str(max(lista)))
print('El menor entero ingresado es: ' + str(min(lista)))
