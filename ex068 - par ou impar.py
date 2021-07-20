# IMPORTAÇÕES
import random


print('='*40)
print('VAMOS JOGAR PAR OU IMPAR')
print('='*40)
cont = 0

while True:
    soma = 0
    pc = random.randint(0,11)
    jogador = int(input('digite um valor: '))
    soma = pc + jogador
    jogador1 = ' '
    while jogador1 not in 'PI':
        jogador1 = str(input('PAR OU IMPAR [P/I]? ')).strip()[0].upper()
    if jogador1 == 'P' and soma % 2 == 0:
        print(f'VOCE GANHOU - PAR. Computador escolheu {pc} e voce {jogador} = {soma}')
        cont += 1
    elif jogador1 == 'I' and soma % 2 != 0:
        print(f'VOCE GANHOU - IMPAR. Computador escolheu {pc} e voce {jogador} = {soma}')
        cont += 1
    else:
        print(f'Computador escolheu {pc} e voce {jogador}. total de {soma}')
        print(f'Deu PAr' if soma % 2 == 0 else 'deu Impar')
        break
print(f'VOCE PERDEU. Voce venceu {cont} vezes')
