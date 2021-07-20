n = int(input('digite um nr: '))
contador = 0

if n == 2:
    print(f'{n} é primo - LINHA 3')
elif n % 2 == 0:
    print(f'{n} NÃO É PRIMO - LINHA 5')
else:
    for c in range(1, n+1, 2):
        if n % c == 0:
            contador += 1
    if contador == 2:
        print(f'{n} é primo - linha 13')
    else:
        print(f'{n} não é primo e foi divisivel {contador + 1} vezes - linha 15')

