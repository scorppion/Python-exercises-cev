somaidade = 0
mediaidade = 0
maioridade = 0
nomevelho = ''
mulheresnovas = 0

for p in range(1,5):
    print('-----{}ª pessoa -----'.format(p))
    nome = str(input('nome: ')).strip()
    idade = int(input('idade: '))
    sexo = str(input('sexo: ')).strip().upper()[0]
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridade = idade
        nomevelho = nome
    if sexo in 'Mn' and idade > maioridade:
        maioridade = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        mulheresnovas += 1
mediaidade = somaidade / 4
print('{} mulheres com menos de 20 anos'.format(mulheresnovas))
print('Media idade {}'.format(mediaidade))
print('Homem mais velho {} tem {} anos'.format(nomevelho,maioridade))
