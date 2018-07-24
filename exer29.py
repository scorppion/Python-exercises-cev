velocidade = int(input('Digite a velocidade do veiculo:'))
limite = 80
if velocidade > limite:
    multa = (velocidade - 80)*7
    print('Você ultrapassou o limite de velocidade e irá pagar multa no valor de {} reais'.format(multa))
else:
    print('Você está dentro do limite de velocidade permitido')





