#    Exercício 16 da maratona de 3 meses
#    Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados
#    da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
#    e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades
#    de latas de tinta a serem compradas e o preço total.
#    https://wiki.python.org.br/EstruturaSequencial
#    @author Rafael Araújo Chinaglia <chinaglia.rafa@gmail.com>

import math

area = float(input('Quantos m² serão pintados: '))

lata = {
    'litros': 18,
    'valor': 80.0
}

qtd_latas = math.ceil(area / 3 / lata['litros'])

print('Você precisa comprar', qtd_latas, 'latas. Total a ser pago: R$' + str(format(qtd_latas*lata['valor'], '.2f')))