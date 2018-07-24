maior = menor = 0
valores = list()
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]
print(f'Você digitou os valores {valores}')
print()
print(f'O maior número digitado foi {maior} nas posições ', end=' ')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...')
print()
print(f'O menor número digitado foi {menor} nas posições ', end=' ')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...')


