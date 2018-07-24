while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        print('Programa Encerrado')
        break
    for i in range(1,11):
        m = i * n
        print(f'{n} x {i} = {m}')

