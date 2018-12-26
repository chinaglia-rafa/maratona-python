import re
import sys


def bytes_to_mb(v):
    """
    converte uma quantidade de bytes em megabytes
    :param v: valor em bytes
    :return: valor em mb
    """
    return v / 1048576


def percent_from_total(v, total):
    """
    Encontra a porcentagem ocupada por v em um total
    :param v: valor em bytes
    :param total: valor total em bytes
    :return: porcentagem
    """
    return format((v * 100) / total, '.2f')


order_field = ''
order_field_desc = False
#   detectando argumentos
if len(sys.argv) > 1:
    try:
        pos = sys.argv.index('-o')
        if pos > 0:
            if sys.argv[pos+1] != '':
                order_field = sys.argv[pos+1]
            else:
                print('Erro de sintaxe')
                exit()
            if sys.argv[pos+2] != '':
                if sys.argv[pos+2] == 'asc':
                    pass
                elif sys.argv[pos+2] == 'desc':
                    order_field_desc = True
                else:
                    print('Erro de sintaxe')
                    exit()
    except Exception as err:
        pass

filename = 'usuarios.txt'

try:
    f1 = open(filename, 'r')
except Exception as err:
    print('Ocorreu um erro ao ler os dados:', err)
    exit()

users = []
tt_bytes = 0

for linha in f1:
    dados = re.findall(r'(\w+)\s*(\d+)', linha)
    users.append({
        'username': dados[0][0],
        'disk_size': int(dados[0][1]),
        'disk_in_mb': bytes_to_mb(int(dados[0][1])),
        'percent': 0
    })
    tt_bytes += int(dados[0][1])

f1.close()

if order_field not in ('username', 'usage'):
    print('Você só pode ordenar usando username ou usage')
    exit()
else:
    if order_field == 'username':
        users = sorted(users, key=lambda k: k['username'], reverse=order_field_desc)
    elif order_field == 'usage':
        users = sorted(users, key=lambda k: k['disk_size'], reverse=order_field_desc)

try:
    fs = open('relatorio.txt', 'w')
except Exception as err:
    print('Ocorreu um erro ao criar o arquivo de saída:', err)
    exit()

fs.write('ACME Inc.           Uso do espaço em disco pelos usuários\n')
fs.write('------------------------------------------------------------------------\n')
fs.write('Nr.  Usuário        Espaço utilizado     % do uso\n\n')

indice = 1

for user in users:
    #   calcula a porcentagem de uso de disco
    user['percent'] = percent_from_total(user['disk_size'], tt_bytes)
    #   grava os dados no novo arquivo
    linha = str(indice).ljust(5)
    linha += user['username'].ljust(15)
    linha += format(user['disk_in_mb'], '.2f').rjust(14)
    linha += ' MB'
    linha += user['percent'].rjust(11)+'%'
    linha += '\n'
    fs.write(linha)
    indice += 1

fs.write('\n')
fs.write('Espaço total ocupado: ' + format(bytes_to_mb(tt_bytes), '.2f') + ' MB\n')
fs.write('Espaço médio ocupado: ' + format(bytes_to_mb(tt_bytes / len(users)), '.2f') + ' MB')
