dicjogador = dict()
listagol = list()

dicjogador['nome'] = str(input('qual o nome do jogador: '))
dicjogador['jogos'] = int(input(f'qtas partidas {dicjogador["nome"]} jogou:  '))

for x in range(0, dicjogador["jogos"]):
    gols = int(input(f'qtos gols fez na partida {x + 1}? '))
    listagol.append(gols)
dicjogador['gols'] = listagol[:]
total = sum(listagol)
dicjogador['total'] = total

print('=-'*40)
print(dicjogador)
print('=-'*40)

for k, v in dicjogador.items():
    print(f'o campo {k} tem o valor {v}')
print('=-'*40)

print(f'o {dicjogador["nome"]} jogou {dicjogador["jogos"]} partidas.')

for i in range(0, len(dicjogador["gols"])):
    print(f'=> Na partida {i + 1}, fez {dicjogador["gols"][i]} gols.')
print(f'Foi um total de {dicjogador["total"]}')
