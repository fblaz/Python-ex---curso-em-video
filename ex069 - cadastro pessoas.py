lista = []
i = 0
sexo = " "
homens = 0  # quantos homens foram cadastrados
maioridade = 0  # pessoas com mais de 18
meninas = 0  # mulheres menores de 20

while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Idade: '))
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    lista.insert(i, (idade, sexo))
    i += 1
    sexo = " "
    print('-' * 20)
    loop = " "
    while loop not in "SN":
        loop = str(input('quer continuar? [S/N] ')).strip().upper()[0]
    if loop == 'N':
        print(lista)
        print(len(lista))
        break

for c in range(0, len(lista)):
    if lista[c][0] >= 18:
        maioridade += 1
    if lista[c][1] == 'M':
        homens += 1
    if lista[c][1] == 'F' and lista[c][0] < 20:
        meninas += 1
print(f'pessoas com mais de 18 anos = {maioridade}')
print(f'homens cadastrados = {homens}')
print(f'mulheres menores de 20 = {meninas}')
