sexo = str(input('Digite o sexo da pessoa [M/F]:')).strip().upper()[0]

while sexo not in 'MnFf':

    print('sexo inválido')
    sexo = str(input('Digite o sexo da pessoa [M/F]:')).strip().upper()[0]
else:
    print('Fim')