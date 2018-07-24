a = float(input('Digite o primeiro valor: '))
b = float(input('Digite o segundo valor: '))

if a > b:
    print('O numero {} é maior que {}'.format(a,b))
elif b > a:
    print('O numero {} é maior que {}'.format(b,a))
else:
    print('Os valores são iguais')

