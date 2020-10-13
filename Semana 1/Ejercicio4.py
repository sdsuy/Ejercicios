# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 12:07:26 2020

@author: Santiago
"""

nota = input('Ingrese una nota entre 0 y 100 ')
nota = int(nota)

if nota < 0 or nota > 100:
    print('La nota ingresada no es valida')
else:
    if nota <= 24:
        print('El estudiante recursa')
    elif nota <= 59:
        print('El estudiante puede dar examen')
    else:
        print('El estudiante exonera')
