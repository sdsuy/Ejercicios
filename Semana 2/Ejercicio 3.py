# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 16:33:09 2020

@author: Santiago
"""

def carga_keyword():
    '''
    lee un archivo keywords.txt que debe contener 1 palabra clave por linea
    '''
    file = open('keywords.txt', 'r')
    return file.readlines()

keywords = []

while True:
    
    print('* [1] - Importar palabras clave')
    print('* [2] - Mostrar palabras clave')
    print('* [0] - Salir')
    
    op = input()
    
    if op == '1':
        keywords = carga_keyword()
    elif op == '2':
        n=0
        for keyword in keywords:
            print(keyword.strip() + ' ', end='')
            n+=1
            if n%5==0:
                print()
        print()
    elif op == '0':
        break
