numeros = []
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
    else:
        print(f'Valor duplicado!')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar?[S/N] ')).upper().strip()[0]
    if resp in 'N':
        break
print(f'Os numeros digitados em ordem {sorted(numeros)}')


