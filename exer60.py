'''from math import factorial
num = int(input('Digite um número inteiro: '))
f = factorial(num)
print('O fatorial de {} é {}'.format(num,f))'''

num = int(input('Digite um número inteiro: '))
f = 1
c = num
while c > 0:
    f *= c
    c -= 1
print('O fatorial de {} é {}'.format(num,f))



