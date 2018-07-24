dados = []
pessoas = []
leves = []
pesadas = []
mai = men = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    if len(pessoas) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar?')).strip().upper()[0]
    if resp in 'N':
        break
print('-'*30)
print(f'Total de pessoas cadastradas {len(pessoas)}')
print()
print(f'O maior peso foi {mai} kg ', end='')
for p in pessoas:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi {men} kg ', end='')
for p in pessoas:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')


