preco = total = totmil = menor = cont = 0
nomeMenor = ' '

while True:
    nome = str(input('Nome do produto: '))
    preco = int(input('Preço R$ '))
    total += preco
    cont += 1
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        nomeMenor = nome
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if continuar in 'Nn':
        break
print(f'O total gasto foi de {total}')
print(f'{totmil} produto(s) custa(m) mais de R$ 1000')
print(f'O produto mais barato é {nomeMenor} que custa R$ {menor}')



