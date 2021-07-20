import random

print('=-'*20)
print(f'{"JOKENPO":^40}')
print('=-'*20)
print('SUAS OPÇÕES:')
print('[0] PEDRA')
print('[1] PAPEL')
print('[2] TESOURA')
jokenpo = ['PEDRA', 'PAPEL', 'TESOURA']
pc = random.randrange(0, 2, 1)
pc1 = jokenpo[pc]

player1 = 3
while player1 > 2:
    player1 = int(input('qual sua jogada: '))
player = jokenpo[player1]


if player1 == 0 and pc == 2:
    print('=-'*15)
    print(f'voce escolheu {player}')
    print(f'o computador escolheu {pc1}')
    print('=-' * 15)
    print('VOCE GANHOU!!')
elif pc == 0 and player1 == 2:
    print('=-' * 15)
    print(f'voce escolheu {player}')
    print(f'o computador escolheu {pc1}')
    print('=-' * 15)
    print('COMPUTADOR GANHOU!!')
elif pc == player1:
    print('=-' * 15)
    print(f'voce escolheu {player}')
    print(f'o computador escolheu {pc1}')
    print('=-' * 15)
    print('EMPATOU')
elif pc > player1:
    print('=-' * 15)
    print(f'voce escolheu {player}')
    print(f'o computador escolheu {pc1}')
    print('=-' * 15)
    print('COMPUTADOR GANHOU!!')
else:
    print('=-' * 15)
    print(f'voce escolheu {player}')
    print(f'o computador escolheu {pc1}')
    print('=-' * 15)
    print('VOCE GANHOU!!')
