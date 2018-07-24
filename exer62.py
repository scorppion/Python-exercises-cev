primeiro = int(input('Digite um número: '))
razao = int(input('Digite a razão: '))

termo = primeiro
cont = 1
while cont < 10:
    termo += razao
    print('{}'.format(termo))
    cont += 1
mais = int(input('Deseja mostrar mais quantos termos? '))
cont2 = 1
qtd = mais +1
while cont2 < qtd:
    termo += razao
    print('{}'.format(termo))
    cont2 += 1
else:
    exit()

