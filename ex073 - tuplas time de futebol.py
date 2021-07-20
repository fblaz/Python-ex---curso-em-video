times = ('Flamengo', 'Internacional', 'Atletico-MG', 'São Paulo', 'Fluminense', 'Gremio',
         'Palmeiras', 'Santos', 'Atletico-PR', 'RB Bragantino', 'Ceara', 'Corinthians',
         'Atletico-GO', 'Bahia', 'Sport', 'Fortaleza', 'Vasco', 'Goias', 'Coritiba', 'Botafogo')

print(times)
print(f'=-'*40)

print(f'os 5 primeiros colocados são: {times [0:5]}')
print(f'os 4 ultimos colocados são: {times [-4:]}')
print(f'times em ordem alfabetica {sorted(times)}')
print(f'o São Paulo terminou em {times.index("São Paulo") + 1}ª')

### while True:
    #posicao = ' '
    #while posicao not in times:
        #posicao = str(input('qual time quer pesquisar: ')).lower().strip()
        #if posicao in times().lower():
           # print(f'o time {posicao} terminou em {times.index(posicao)}') ###


