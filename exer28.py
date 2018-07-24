import random

pc = random.randrange(10)
user = int(input('Digite um número inteiro de 0 à 10: '))
if pc == user:
    print('Parabéns você acertou!')
else:
    print('Número {} errado, número certo {}.tente novamente!'.format(user,pc))
