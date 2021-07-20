lista = []

while True:
    num = int(input('digite um nr: '))
    lista.append(num)
    loop = ' '
    while loop not in 'SN':
        loop = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if loop == 'N':
        break


print(sorted(lista, reverse=True))

print(f'foram digitados {len(lista)} numeros')
print(f'o valor 5 foi digitado na lista' if 5 in lista else 'o valor 5 não foi digitado')