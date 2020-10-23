# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 12:54:15 2020

@author: Santiago
"""

import numpy as np
rng = np.random.default_rng()

def puntosCirculo(n):
    circulo = 0
    # genero 2 listas de numeros aleatorias entre 0.0 y 1.0
    x, y = rng.random(n), rng.random(n)
    # para cada par de elementos en x e y recorro ambas listas en paralelo
    for a, b in zip(x, y):
        # si se cumple la ecuacion cfa
        # significa que esta dentro del rango 0, 1
        if (a**2 + b**2) ** 0.5 <= 1:
            # incremento circulo
            circulo += 1
    return (4*circulo)/n
        
%time print(puntosCirculo(10))
%time print(puntosCirculo(int(1e2)))
%time print(puntosCirculo(int(1e3)))
%time print(puntosCirculo(int(1e4)))
%time print(puntosCirculo(int(1e5)))
%time print(puntosCirculo(int(1e6)))
%time print(puntosCirculo(int(1e7)))
