from datetime import datetime
nasc = int(input('Digite o ano de seu nascimento: '))

now = datetime.now()

idade = now.year - nasc

if idade <= 17:
    falta = 18 - idade
    print('Você tem {} anos e ainda falta {} ano(s) pra se alistar no exercíto'.format(idade,falta))
elif idade == 18:
    print('Você tem {} anos e está na hora de se alistar'.format(idade))
else:
    atraso = idade - 18
    print('Você tem {} anos e já passou {} ano(s) do prazo para se alistar no exercíto'.format(idade,atraso))