import math

ang = float(input('Digite um ângulo: '))

seno = math.sin(ang)

coseno = math.cos(ang)

tangente = math.tan(ang)

print('O seno do ângulo {} é igual a {:.2f}'.format(ang,seno))

print('O coseno do ângulo {} é igual a {:.2f}'.format(ang,coseno))

print('A tangente do ângulo {} é igual a {:.2f}'.format(ang,tangente))