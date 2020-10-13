# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 11:06:28 2020

@author: Santiago
"""

print('p) perimetro de un triangulo')
print('s) superficie de un rectangulo')
print('v) volumen de un prisma')
op = input('Ingrese una opcion: ')

if op == 'p':
    a = input('Ingrese lado a ')
    b = input('Ingrese lado b ')
    c = input('Ingrese lado c ')
    perimetro = int(a) + int(b) + int(c)
    print('El perimetro del triangulo es ' + str(perimetro))
elif op == 's':
    a = input('Ingrese lado a ')
    b = input('Ingrese lado b ')
    superficie = int(a) * int(b)
    print('La superficie del rectangulo es ' + str(superficie))
elif op == 'v':
    h = input('Ingrese altura h ')
    a = input('Ingrese ancho a ')
    b = input('Ingrese largo b ')
    volumen = int(h) * int(a) * int(b)
    print('El volumen del prisma es ' + str(volumen))
else:
    print('Opcion invalida')
