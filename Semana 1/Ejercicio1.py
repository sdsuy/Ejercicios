# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 23:18:57 2020

@author: Santiago
"""

valor = input('Ingrese la longitud a calcular ')
unidad = input('Ingrese la unidad de medida del valor ingresado (milla, pie o pulgada) ')

if unidad == 'milla':
    print(float(valor) * 1609.34)
elif unidad == 'pie':
    print(float(valor) * 0.3048)
elif unidad == 'pulgada':
    print(float(valor) * 0.0254)
else:
    print('Opcion invalida')