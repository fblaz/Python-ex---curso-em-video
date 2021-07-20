num = int
loop = ' '
lista = []
i = 0

while True:
    num = int(input('digite um numero: '))
    if num not in lista:
        lista.append(num)
        print('valor adicionado com sucesso')
    else:
        print('valor duplicado! não vou adicionar')
    loop = ' '
    while loop not in 'SN':
        loop = str(input('quer continuar? [S/N] ')).upper().strip()[0]
    if loop == 'N':
        print('=-'*20)
        print('obrigado, lista cadastrada')
        break
lista.sort()
print(lista)