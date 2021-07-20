tupla = (int(input('digite um nr: ')),
         int(input('digite um nr: ')),
         int(input('digite um nr: ')),
        int(input('digite um nr: ')))


print(tupla)
print(f'o nove apareceu - {tupla.count(9)} vezes')
print(f'o 3 foi digitado primeiro na posicao {tupla.index(3) + 1} ' if 3 in tupla else 'não foi digitado 3')
print(f'nrs pares digitados: ', end="")
for c in range(0, (len(tupla))):
    if tupla[c] % 2 == 0:
        print(f' {tupla[c]}', end=" ")