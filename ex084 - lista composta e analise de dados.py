lista = []  # lista de pessoas
temp = []  # lista temporaria para incluir as pessoas em lista
cont = 0  # conta qtas pessoas foram cadastradas
pesado = []  # lista das pessoas mais pesadas
leve = []  # lista das pessaos mais leves
maior = 0
menor = 0

while True:
    nome = str(input('digite o nome da pessoa: ')).upper()
    peso = float(input('digite o peso da pessoa: '))
    if len(lista) == 0:
        maior = peso
        menor = peso
    elif peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
    temp.append(nome)
    temp.append(peso)
    lista.append(temp[:])
    temp.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break

for p, k in enumerate(lista):
    if k[1] == maior:
        pesado.append(k[0])
    if k[1] == menor:
        leve.append(k[0])

cont = len(lista)

print(f'foram cadastradas {cont} pessoas')
print(f'as pessoas mais pesadas com {maior}kg são {sorted(pesado)}')
print(f'as pessoas mais leves com {menor}kg são {sorted(leve)}')
