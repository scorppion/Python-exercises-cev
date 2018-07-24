import random

pc = random.randrange(10)
user = int(input('Digite um número inteiro de 0 à 10: '))

cont = 0
while user != pc:
    print('Número {} errado, tente novamente!'.format(user))
    user = int(input('Digite um número inteiro de 0 à 10: '))
    cont += 1
else:
    print('Parabéns você acertou em {} tentativa(s)!'.format(cont))