lista = []
par = []
impar = []
num = 0

while True:
    num = int(input('digite um nr: '))
    lista.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp in 'N':
        print('FIM DO PROGRAMA')
        print('=-'*20)
        break
print(f'a lista digitada foi: {sorted(lista)}')
print(f'a lista de pares é: {sorted(par)}')
print(f'a lista de impares é: {sorted(impar)}')