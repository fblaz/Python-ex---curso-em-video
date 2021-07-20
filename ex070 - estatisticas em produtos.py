# IMPORTAÇÕES
import math


print('-' * 20)
print('LOJA SUPER BARATÃO')
print('-' * 20)

lista = []
total = 0  # total gasto na compra
contador = 0  # produtos mais de 1 mil reais
i = 0  # contador da lista


while True:
    prod = str(input('nome do produto: ')).strip().lower()
    preco = float(input('preço do produto: R$ '))
    lista.insert(i, (prod, preco))
    total += preco
    loop = ' '
    while loop not in 'SN':
        loop = str(input('quer continuar [S/N]? ')).strip().upper()[0]
        i += 1
    if loop == "N":
        print('FIM DAS COMPRAS')
        print(lista)
        break

barato = lista[0][1]  # pega o primeiro termo da lista (preco)
baratonome = lista[0][0]  # pega o primeiro termo da lista (prod)

for c in range(0, len(lista)):
    if lista[c][1] > 1000:
        contador += 1
    if lista[c][1] < barato:
        barato = lista[c][1]
        baratonome = lista[c][0]

print(f'R$ {total:.2f} é o valor gasto das compras')
print(f'{lista[0][0]} é o produto com menor preço e valor R$ {barato:.2f} ')
print(f'{contador} produtos com preço maior que 1 mil reais')

