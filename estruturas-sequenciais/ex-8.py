'''
    Exercício 8 da maratona de 3 meses
    Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre
    o total do seu salário no referido mês.
    https://wiki.python.org.br/EstruturaSequencial
    @author Rafael Araújo Chinaglia <chinaglia.rafa@gmail.com>
'''

valor_hora = float(input('Quanto você ganha por hora: '))
horas = int(input('Horas trabalhadas no mês: '))

print('Salário no mês =', valor_hora * horas)