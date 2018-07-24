tab = ('Flamengo', 'Atlético M.', 'São Paulo', 'Internacional','Grêmio', 'Palmeiras', 'Sport', 'Cruzeiro',
       'Botafogo', 'Corinthians', 'Vasco', 'Fluminense', 'América', 'Chapecoense', 'Santos', 'Vitoria',
       'Bahia', 'Paraná', 'Atlético PR', 'Ceará')
print(f'Os 5 primeiros colocados: {tab[0:5]} ')
print(f'Os 4 últimos colocados: {tab[16:]} ')
print(f'Em ordem alfabética: {sorted(tab)}')
for pos, time in enumerate(tab):
    if time in 'Chapecoense':
        print(f'A Chapecoense está na posição {pos +1}')
    #print(f'{time} está na posição {pos +1}')
