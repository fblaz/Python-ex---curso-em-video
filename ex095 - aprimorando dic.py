dicjogador = dict()
listagol = list()
listajogador = list()


while True:
    dicjogador['nome'] = str(input('qual o nome do jogador: '))
    dicjogador['jogos'] = int(input(f'qtas partidas {dicjogador["nome"]} jogou:  '))

    for x in range(0, dicjogador["jogos"]):
        gols = int(input(f'qtos gols fez na partida {x + 1}? '))
        listagol.append(gols)
    dicjogador['gols'] = listagol[:]
    total = sum(listagol)
    dicjogador['total'] = total
    listajogador.append(dicjogador.copy())
    listagol.clear()

    while True:
        resp = str(input('quer continuar: [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! DIGITE S OU N')
    if resp == 'N':
        break

print('=-'*40)
print(listajogador)
print('=-'*40)
print(f'{"cód"}', end="")
for i in dicjogador.keys():
    print(f'{i:<15}', end="")
print()

for i, v in enumerate(listajogador):
    print(f"{i:>3}", end="")
    for d in v.values():
        print(f' {str(d):<15}', end="")
    print()
print('=-'*40)

while True:
    mostra = int(input('mostrar os dados de qual jogador? 999 para parar: '))
    while mostra != 999 and mostra > len(listajogador) - 1:
        print('Erro, não existe o cod jogador')
        mostra = int(input('mostrar os dados de qual jogador? 999 para parar: '))

    if mostra == 999:
        break
    else:
        print(f'LEVANTAMENTO DO JOGADOR {listajogador[mostra]["nome"]}')
        for i in range(0, len(listajogador[mostra]["gols"])):
            print(f'=> Na partida {i + 1}, fez {listajogador[mostra]["gols"][i]} gols.')
        print(f'Foi um total de {listajogador[mostra]["total"]}')