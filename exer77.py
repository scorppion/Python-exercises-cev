palavras = ('Programar', 'Estudar', 'Trabalhar', 'Comer', 'Jogar', 'Digitar', 'JJ')
for p in palavras:
    print(f'\n Na palavra {p} temos ', end='')
    for vogal in p:
        if vogal.lower() in 'aeiou':
            print(vogal, end=' ')

