import random
import time


jogos = []
lista = []
num = 0

apostas = int(input('quantos jogos deseja fazer? '))

for c in range(0, apostas):
    jogos = random.sample(range(0, 61), 6)
    lista.append(sorted(jogos[:]))
    jogos.clear()

print('=-' * 3, f'SORTEANDO {apostas} JOGOS', '=-' *3 )
for j in range(0, len(lista)):
    print(f'jogo {j+1}: {lista[j]}')
    time.sleep(0.5)