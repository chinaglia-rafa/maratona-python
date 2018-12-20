'''
    Exercício 7 da maratona de 3 meses
    Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
    https://wiki.python.org.br/EstruturaSequencial
    @author Rafael Araújo Chinaglia <chinaglia.rafa@gmail.com>
'''

lado = float(input('Digite o tamanho do lado do quadrao: '))

area = lado * lado

print('A area do quadrado é', area, 'e o dobro é', area * 2)