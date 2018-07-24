import random
cont = 0
while True:
    nUser = int(input('Digite um número: '))
    escUser = ' '
    while escUser not in 'PI':
        escUser = str(input('Impar ou Par? [I/P]: ')).upper().strip()[0]
    nPC = random.randrange(11)
    soma = nUser + nPC
    escPC = ' '
    if escUser in 'Ii':
        escPC == 'Pp'
    else:
        escPC == 'Ii'

    if soma %2 == 0 and escUser in 'Pp':
        print(f'Você jogou {nUser} o PC jogou {nPC}. O total foi {soma} deu PAR')
        print('Você venceu! Vamos continuar ...')
        cont +=1
    elif soma %2 == 0 and escUser in 'Ii':
        print(f'Você jogou {nUser} o PC jogou {nPC}. O total foi {soma} deu PAR')
        print('Você perdeu')
        break
    elif soma %2 == 1 and escUser in 'Ii':
        print(f'Você jogou {nUser} o PC jogou {nPC}. O total foi {soma} deu IMPAR')
        print('Você venceu! Vamos continuar ...')
        cont +=1
    else:
        print(f'Você jogou {nUser} o PC jogou {nPC}. O total foi {soma} deu IMPAR')
        print('Você perdeu')
        break
print(f'Total de pontos {cont}')


