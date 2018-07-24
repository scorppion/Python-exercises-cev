lista = ('Pão', 1.20, 'Leite', 2.50, 'Café', 1.50, 'Açucar', 2.10, 'Arroz', 10.80)
print('-' * 40)
print(f'{"Listagem de preços":^40}')
print('-' * 40)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R${lista[pos]:>7.2f}')
print('-' * 40)
