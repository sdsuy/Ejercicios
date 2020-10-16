# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 15:57:22 2020

@author: Santiago
"""

n = input('n=')
lista = input('Ingrese ' + n + ' enteros: ')
lista = lista.split()
if len(lista) != int(n):
    raise Exception('no ingresó ' + n + ' numero/s, intentalo nuevamente')
print('El mayor entero ingresado es: ' + str(max(lista)))
print('El menor entero ingresado es: ' + str(min(lista)))
