lista = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
         'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
         'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    while True:
        num = int(input('digite um nr entre 0 e 20: '))
        if 0 <= num <= 20:
            break
    print(f'o numero digitado foi {lista[num]} = {num}')
    loop = " "
    while loop not in 'SN':
        loop = str(input(('Voce deseja continuar? [S/N] '))).upper().strip()[0]
    if loop == 'N':
        break
print('FIM DO PROGRAMA')
