num = int(input('Digite um número: '))
tot = 0

for i in range(1,num +1):
    if num % i == 0:
        tot += 1
if tot == 2:
    print(' o número {} é primo pois só é divisivel por 1 e por ele mesmo'.format(i))
else:
    print(' o número {} não é primo pois foi divisivel {} vezes'.format(i,tot))

