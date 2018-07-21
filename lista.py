lista = []
par = []
impar = []
while True:
    lista.append(int(input('Digite um número: ')))
    resp = ' '
    while resp not in 'NS':
        resp = str(input('Deseja continuar ?[S/N]')).strip().upper()[0]
    if resp in 'N':
        break
for n in lista:
    if n %2 == 0:
        par.append(n)
    else:
        impar.append(n)
print('Números da lista: {}'.format(lista))
print('Números pares da lista: {}'.format(par))
print('Números impares da lista: {}'.format(impar))


