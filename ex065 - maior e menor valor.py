import math


flag = 's'
lista = []
cont = 0
soma = 0

while flag != 'n':
    x = int(input('digite um nr: '))
    lista.insert(cont, x)
    cont += 1
    soma += x
    flag = str(input('quer continuar? [S/N] ')).strip()[0].lower()
print(f'voce digitou {len(lista)} numeros')
print(f'a media é {soma / len(lista)}')
print(f'o maior valor foi {max(lista)}')
print(f'o menor valor foi {min(lista)}')
print(lista)
print(f'{math.fsum(lista[0:])/len(lista)} é a media')

