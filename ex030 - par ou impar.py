# IMPORTACOES

# FUNCOES

def parimpar(num):
    calc = num % 2
    if calc == 0:
        return 'par'
    else:
        return'impar'


# PROGRAMA PRINCIPAL

x = int(input('digite um nr: '))
if parimpar(x) == 'par':
    print(f'numero {x} é par')
else:
    print(f'numero {x} é impar')
