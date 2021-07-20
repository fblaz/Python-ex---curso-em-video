import random


num = random.randint(0,10)
tentativa = 0
n1 = int(input('qual o nr que pensei? '))

while n1 != num:
    if n1 < num:
        print('Mais...')
        n1 = int(input('Ainda não. qual o numero que pensei de 0 a 10? '))
        tentativa += 1
    else:
        print('Menos...')
        n1 = int(input('Ainda não. qual o numero que pensei de 0 a 10? '))
        tentativa += 1

print('-'*20)
print(f'Acertou. Pensei no nr {num}\n'
      f'voce tentou {tentativa + 1} vezes')