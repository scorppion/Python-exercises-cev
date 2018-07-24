lista = []
par = []
impar = []
while True:
    lista.append(int(input('Digite um valor: ')))

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if resp in 'N':
        break
for n in lista:
    if n % 2 == 0:
        par.append(n)
for n in lista:
    if n % 2 != 0:
        impar.append(n)
print(f'A lista completa {sorted(lista)}')
print(f'A lista dos pares {sorted(par)}')
print(f'A lista dos impares {sorted(impar)}')

