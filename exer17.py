import math
o = float(input('Digite o cateto oposto: '))
a = float(input('Digite o cateto adjacente: '))

#c = (a**2 + o**2)

h = math.hypot(o,a)

print(' Valor da hipotenuza {:.2f}'.format(h))
