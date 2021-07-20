matriz = [[], [], []]
num = 0

for l in range(0, 3):
    for c in range(0, 3):
        num = int(input(f'digite a posição {[l, c]}: '))
        matriz[l].append(num)

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{(matriz[l][c]):^3}]', end='')
    print()
