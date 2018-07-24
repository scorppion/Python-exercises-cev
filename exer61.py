primeiro = int(input('Digite um número: '))
razao = int(input('Digite a razão: '))

termo = primeiro
cont = 1
while cont < 10:
    termo += razao
    print('{}'.format(termo))
    cont += 1


