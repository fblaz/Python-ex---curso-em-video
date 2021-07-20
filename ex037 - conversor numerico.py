# PRINCIPAL

x = int(input('digite um nr: '))
y = int(input('CONVERSÃO, digite:\n'
              ' 1 para binario,\n'
              ' 2 para octal\n'
              ' 3 para hexadecimal: '))
if y == 1:
    print(f'o numero \033[1;31m{x}\033[m em formato BINARIO é \033[1;32m{bin(x)}\033[m')
elif y == 2:
    print(f'o numero \033[1;31m{x}\033[m em formato OCTAL é \033[1;32m{oct(x)}\033[m')
elif y == 3:
    print(f'o numero \033[1;31m{x}\033[m em formato HEXADEXIMAL é \033[1;32m{hex(x)}\033[m')


