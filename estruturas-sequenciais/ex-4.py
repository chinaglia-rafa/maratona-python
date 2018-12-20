'''
    Exercício 4 da maratona de 3 meses
    Faça um Programa que peça as 4 notas bimestrais e mostre a média.
    https://wiki.python.org.br/EstruturaSequencial
    @author Rafael Araújo Chinaglia <chinaglia.rafa@gmail.com>
'''

soma = 0
for i in range(4):
    soma += int(input('Digite a ' + str(i+1) + 'ª nota: '))

print('A média é', soma / 4)
