

casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o valor do seu salário: '))
anos = int(input('Informe em quantos anos irá pagar: '))

prestação = (casa/12)/anos

salarioTrinta = (salario/100)*30

if prestação > salarioTrinta:
    print('Financiamento não aprovado, o valor da prestação R$ {:.2f} é maior que 30% do seu salário R$ {:.2f}'.format(prestação,salarioTrinta))
else:
    print('Financiamento aprovado! Valor da prestação mensal {:.2f} '.format(prestação))

