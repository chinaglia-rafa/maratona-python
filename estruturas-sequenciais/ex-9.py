'''
    Exercício 9 da maratona de 3 meses
    Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
    C = (5 * (F-32) / 9).
    https://wiki.python.org.br/EstruturaSequencial
    @author Rafael Araújo Chinaglia <chinaglia.rafa@gmail.com>
'''

farenheit = float(input('Digite a temperatura em farenheit: '))

celsius = (5 * (farenheit - 32) / 9)

print(farenheit, 'farenheit =', str(format(celsius, '.2f')) + 'º Celsius')