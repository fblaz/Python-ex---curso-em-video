# IMPORTAÇÕES


# FUNÇÕES

def multa(velocidade):
    if velocidade > 80:
        print(f'VOCE FOI MULTADO! o limite é de 80 km/h\n'
              f'Voce excedeu o limite em {(velocidade-80):.2f} km/h\n'
              f'Valor da multa R$ {((velocidade - 80)*7):.2f}')
    else:
        print('velocidade dentro dos limites')


# PROGRAMA PRINCIPAL

vel = float(input('digite a velocidade: '))
multa(vel)
