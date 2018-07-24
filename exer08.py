import math

num = int(input('Digite um número: '))

raiz = math.sqrt(num)

print('A raiz de {} é igual a {:.2f}'.format(num,raiz))

print('A raiz de {} arredondada pra mais é igual a {}'.format(num, math.ceil(raiz)))

print('A raiz de {} arredondada pra menos é igual a {}'.format(num, math.floor(raiz)))