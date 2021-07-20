import random, time


print('=-'*50)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('=-'*50)
x = random.randrange(0, 5, 1)
y = int(input('Em qual numero eu pensei? '))
print('PROCESSANDO...')
time.sleep(1)
if x == y:
    print('PARABENS!! Você conseguiu me vencer.')
else:
    print(f'GANHEI!! Eu pensei no numero {x} e não {y}')
