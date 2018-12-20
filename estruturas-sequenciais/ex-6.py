'''
    Exercício 6 da maratona de 3 meses
    Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
    https://wiki.python.org.br/EstruturaSequencial
    @author Rafael Araújo Chinaglia <chinaglia.rafa@gmail.com>
'''

import math

raio = input('Digite o raio do círculo: ')

print('A area do círculo é igual a', (2 * math.pi * float(raio)))