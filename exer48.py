soma = 0
cont = 0
for i in range(1,501,2):
    if i % 3 == 0:
        cont = cont + 1
        soma = soma + i

print('A soma dos multiplos é {} e a quantidade de numeros multiplos de 3 são {}'.format(soma,cont))
