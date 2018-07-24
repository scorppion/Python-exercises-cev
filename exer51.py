primeiro = int(input('Digite um número: '))
razao = int(input('Digite a razão: '))

decimo = primeiro + (10 -1) * razao
for i in range(primeiro,decimo + razao,razao):
     print('{}'.format(i))

