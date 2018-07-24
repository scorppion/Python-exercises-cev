import random
print("""
1 = Pedra
2 = Papel
3 = Tesoura""")

escolha = input('Escolha: ')
maquina = random.choice(['Pedra','Papel','Tesoura'])

if escolha == '1':
    nome = 'Pedra'
elif escolha == '2':
    nome = 'Papel'
elif escolha == '3':
    nome = 'Tesoura'
else:
    print('Escolha uma das opções acima!')
    exit()

if escolha == '1' and maquina == 'Pedra' or escolha == '2' and maquina == 'Papel' and escolha == '3' or maquina =='Tesoura':
    print('Você Escolheu: {}'.format(nome))
    print('A máquina Escolheu: {}'.format(maquina))
    print('Deu Empate!')
elif escolha == '1' and maquina == 'Papel' or escolha == '2' and maquina == 'Tesoura' and escolha == '3' or maquina =='Pedra':
    print('Você Escolheu: {}'.format(nome))
    print('A máquina Escolheu: {}'.format(maquina))
    print('Você PERDEU!')
else:
    print('Você Escolheu: {}'.format(nome))
    print('A máquina Escolheu: {}'.format(maquina))
    print('Você GANHOU!')