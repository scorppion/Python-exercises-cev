from time import sleep
num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))


opção = 0

while opção != 1 or 5:
    opção = int(input('''Escolha uma das opções abaixo:
    1 = Somar
    2 = Multiplicar
    3 = Maior
    4 = Novos números
    5 = Sair
    Qual é a sua escolha? '''))

    if opção == 1:
        soma = num1 + num2
        print('A soma dos números é igual a {} '.format(soma))
    elif opção == 2:
        mult = num1 * num2
        print('A multiplicação dos números é igual a {}'.format(mult))
    elif opção == 3:
        if num1 > num2:
            print('O número {} é maior'.format(num1))
        else:
            print('O número {} é maior'.format(num2))
    elif opção == 4:
        num1 = float(input('Digite um número: '))
        num2 = float(input('Digite outro número: '))
    elif opção == 5:
        exit()
    else:
        print('Opção inválida, tente novamente')
    sleep(2)