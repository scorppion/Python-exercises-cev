p = cont = 0
numeros = (int(input('Digite um número: ')),
           int(input('Digite outro número: ')),
           int(input('Digite mais um número: ')),
           int(input('Digite o último número: ')))
print(f'Você digitou os valores: {numeros}')
print(f'O número 9 foi digitado {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O número 3 está na posição {numeros.index(3)+1}')
else:
    print('O valor 3 não foi digitado')
print(f'Os números pares são ', end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')





