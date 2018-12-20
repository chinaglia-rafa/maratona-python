'''
    Exercício 12 da maratona de 3 meses
    Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
    usando a seguinte fórmula: (72.7*altura) - 58
    https://wiki.python.org.br/EstruturaSequencial
    @author Rafael Araújo Chinaglia <chinaglia.rafa@gmail.com>
'''

altura = float(input('Digite a sua aultura: '))

print('Seu peso ideal seria', format((72.7 * altura) - 58, '.2f') + 'kg')