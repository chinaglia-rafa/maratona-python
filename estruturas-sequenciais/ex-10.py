'''
    Exercício 10 da maratona de 3 meses
    Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.
    F = ((9*C) / 5) + 32
    https://wiki.python.org.br/EstruturaSequencial
    @author Rafael Araújo Chinaglia <chinaglia.rafa@gmail.com>
'''

C = float(input('Digite o valor em graus Celsius: '))

F = ((9*C) / 5) + 32

print(str(C) + 'ºC = ' + str(format(F, '.2f'))+'º Farenheit')