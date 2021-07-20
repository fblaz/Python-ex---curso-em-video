lista = []
num = 0
maior = 0
menor = 0

for c in range(0, 5):
    num = int(input(f'digite o {c + 1}º valor: '))
    lista.insert(c, num)

maior = max(lista)
menor = min(lista)

print(f'Voce digitou os valores {lista}')

print(f'os valores maiores ({maior}) foram digitados nas posições:', end=" ")
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}...',end='')

print(f'\nos valores menores ({menor}) foram digitados nas posições:', end=" ")
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}...', end='')
