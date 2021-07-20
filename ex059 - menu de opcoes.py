n1 = int(input('PRIMEIRO VALOR: '))
n2 = int(input('SEGUNDO VALOR: '))
loop = 0
while loop != 5:
    print('[ 1 ] somar\n'
          '[ 2 ] multiplicar\n'
          '[ 3 ] maior\n'
          '[ 4 ] novos numeros\n'
          '[ 5 ] sair do programa\n' )
    loop = int(input('>>>>> QUAL É A SUA OPÇÃO? '))
    if loop == 1:
        print(f'{n1} + {n2} = {n1 + n2}')
        print('=-'*15)
    elif loop == 2:
        print(f'{n1} x {n2} = {n1 * n2}')
        print('=-' * 15)
    elif loop == 3:
        print(f'{max(n1, n2)} é o maior numero entre {n1} e {n2}')
        print('=-' * 15)
    elif loop == 4:
        n1 = int(input('PRIMEIRO VALOR: '))
        n2 = int(input('SEGUNDO VALOR: '))
        print('=-' * 15)
    elif loop == 5:
        loop = 5
    else:
        loop = int(input('>>>>> OPÇÃO INVALIDA. QUAL É A SUA OPÇÃO? '))
        print('=-' * 15)
print('FIM DO PROGRAMA')