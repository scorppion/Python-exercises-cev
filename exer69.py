pesMaior = 0
masc = 0
mulherMenor = 0
while True:
    idade = int(input('Informe a idade: '))
    if idade > 18:
        pesMaior += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Informe o sexo [M/F]: ')).upper().strip()[0]
        if sexo in 'F' and idade < 20:
            mulherMenor += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [s/n]')).upper().strip()[0]
    if continuar in 'Nn':
        break
    if sexo in 'M':
        masc += 1

print(f'Total de pessoas com mais de 18 anos é de {pesMaior}')
print(f'Total de homens é de {masc}')
print(f'Total de mulheres com menos de 20 é de {mulherMenor}')


