import operator


dic = dict()
lista = list()

while True:
    dic.clear()
    dic['nome'] = str(input('nome: '))
    sexo = str(input('sexo: [M/F] ')).upper().strip()[0]
    while sexo not in 'MF':
        print('ERRO! responda apenas M ou F')
        sexo = str(input('sexo: [M/F] ')).upper().strip()[0]
    dic['sexo'] = sexo
    dic['idade'] = int(input('idade: '))
    lista.append(dic.copy())
    loop = str(input('quer continuar?: [S/N] ')).upper().strip()[0]
    while loop not in 'SN':
        print('ERRO! responda apenas S ou N')
        loop = str(input('quer continuar?: [S/N] ')).upper().strip()[0]
    if loop == 'N':
        break

somaidades = 0
for i in range(0, len(lista)):
    somaidades += lista[i]['idade']

mediaidade = somaidades / (len(lista))

print(lista)
print('=-'*30)
print(f'A) ao todo temos {len(lista)} pessoas cadastradas')
print(f'B) a média de idades é {mediaidade:5.2f} ')

print(f'C) as mulheres cadastradas foram: ', end=" ")
for i in range(0, len(lista)):
    if lista[i]['sexo'] == 'F':
        print(lista[i]['nome'], end=" ")
print()

print(f'D) A lista de pessoas que estão acima de média: ')
for p in lista:
    if p['idade'] > mediaidade:
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()