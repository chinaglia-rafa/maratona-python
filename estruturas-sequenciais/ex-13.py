'''
    Exercício 13 da maratona de 3 meses
    Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
        - Para homens: (72.7*h) - 58
        - Para mulheres: (62.1*h) - 44.7
    https://wiki.python.org.br/EstruturaSequencial
    @author Rafael Araújo Chinaglia <chinaglia.rafa@gmail.com>
'''

sexo = None

while sexo != 'm' and sexo != 'f':
    sexo = input('Você é do sexo masculino [m] ou feminino [f]? ')
    if sexo != 'm' and sexo != 'f':
        print('As unicas opções válidas são "m" e "f"')
altura = float(input('Digite a sua aultura: '))

if sexo == 'm':
    print('Seu peso ideal seria', format((72.7 * altura) - 58, '.2f') + 'kg')
else:
    print('Seu peso ideal seria', format((62.1 * altura) - 44.7, '.2f') + 'kg')
