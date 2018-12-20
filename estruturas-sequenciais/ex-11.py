'''
    Exercício 11 da maratona de 3 meses
    Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
        - o produto do dobro do primeiro com metade do segundo .
        - a soma do triplo do primeiro com o terceiro.
        - o terceiro elevado ao cubo.
    https://wiki.python.org.br/EstruturaSequencial
    @author Rafael Araújo Chinaglia <chinaglia.rafa@gmail.com>
'''


def validate(num):
    try:
        num = int(num)
    except:
        print('ERRO! Digite um numero INTEIRO!')
        exit()
    return num


int1 = input('Digite um numero inteiro: ')
int1 = validate(int1)
int2 = input('Digite outro numero inteiro: ')
int2 = validate(int2)
flt = float(input('Digite um numero real: '))

print('Parte a)', int1 * (int2/2))
print('Parte b)', 3*int1 + flt)
print('Parte c)', flt**3)
