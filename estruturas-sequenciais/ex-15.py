#    Exercício 15 da maratona de 3 meses
#    Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#    Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para
#    o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#       salário bruto.
#       quanto pagou ao INSS.
#       quanto pagou ao sindicato.
#       o salário líquido (salário bruto - descontos).
#       calcule os descontos e o salário líquido
#    https://wiki.python.org.br/EstruturaSequencial
#    @author Rafael Araújo Chinaglia <chinaglia.rafa@gmail.com>

valor_hora = float(input('Quanto você ganha por hora trabalhada: '))
horas = int(input('Quantas horas você trabalhou esse mês: '))

salario_bruto = valor_hora * horas
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sind = salario_bruto * 0.05

liquido = salario_bruto - ir - inss - sind

print('Seu salário bruto é R$' + str(format(salario_bruto, '.2f')))
print('Descontos:')
print('IR: R$' + str(format(ir, '.2f')))
print('INSS: R$' + str(format(inss, '.2f')))
print('Sindicato: R$' + str(format(sind, '.2f')))
print('---------------------------')
print('Seu salário líquido é R$' + str(format(liquido, '.2f')))
