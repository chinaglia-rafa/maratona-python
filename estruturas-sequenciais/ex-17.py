#    Exercício 16 da maratona de 3 meses
#    Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
#    pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida
#    em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#       Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#       comprar apenas latas de 18 litros;
#       comprar apenas galões de 3,6 litros;
#       misturar latas e galões, de forma que o preço seja o menor.
#           Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
#    https://wiki.python.org.br/EstruturaSequencial
#    @author Rafael Araújo Chinaglia <chinaglia.rafa@gmail.com>

import math

area = float(input('Quantos m² serão pintados: '))

eficiencia = 6

lata = {
    'litros': 18,
    'valor': 80.0
}

galao = {
    'litros': 3.6,
    'valor': 25.0
}

qtd_latas = math.ceil(area / eficiencia / lata['litros'])
qtd_galao = math.ceil(area / eficiencia / galao['litros'])

qtd_lata_misto = round(area / eficiencia / lata['litros'])
area_restante = area - qtd_lata_misto * lata['litros'] * eficiencia
qtd_galao_misto = math.ceil(area_restante / eficiencia / galao['litros'])

total_misto = qtd_galao_misto * galao['valor'] + qtd_lata_misto * lata['valor']

print(area_restante)

print('=== LATAS ====')
print('Você precisa comprar', qtd_latas, 'latas. Total a ser pago: R$' + str(format(qtd_latas*lata['valor'], '.2f')))
print('=== GALÕOES ====')
print('Você precisa comprar', qtd_galao, 'galões. Total a ser pago: R$' + str(format(qtd_galao*galao['valor'], '.2f')))
print('=== MISTO ====')
print('Você precisa comprar', qtd_lata_misto, 'lata(s) e', qtd_galao_misto,
      'galão(ões). Total a ser pago: R$' + str(format(total_misto, '.2f')))
