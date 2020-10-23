# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 17:25:29 2020

@author: Santiago
"""

import numpy as np

a = np.array([
        [1, 2, 5, 6],
        [4, -4, -6, 8],
        [-12, 1, 3, 9],
        [18, 0, 3, 0]
    ])
b = np.array([1, 6, 7, 2])
x = np.linalg.solve(a, b)

a = np.array([
        [1, 2, 1],
        [0, 1, 1],
        [1, 0, 1]
    ])
b = np.array([4, 3, 5])
y = np.linalg.solve(a, b)

a = np.array([
        [36, 51, 13],
        [52, 34, 74],
        [0, 7, 1.1]
    ])
b = np.array([3, 45, 33])
z = np.linalg.solve(a, b)

a = np.array([
        [3, 9, -10],
        [1, -6, 4],
        [10, -2, 8]
    ])
b = np.array([24, -4, 20])
u = np.linalg.solve(a, b)
