print('Digite 999 para sair')
soma = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    soma += n
print(f'A soma é igual a {soma}')
