print('Maior/Menor/Media')
soma = cont = media = 0
resp = 'S'
while resp in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
media = soma / cont

print(f'A quantidade de numeros digitados foi {cont} a soma é {soma}, a media é igual a {media}')
print(f'O maior valor digitado foi {maior} e o menor foi {menor}')