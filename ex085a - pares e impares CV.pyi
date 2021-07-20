num = [[], []]
valor = 0

for c in range(1, 8):
    valor = int(input(f'digite o {c}º valor: '))
    if valor % 2:
        num[0].append(valor)
    else:
        num[1].append(valor)
print(f'os valores são: {num}')
print(f'os valores pares são: {sorted(num[0])}')
print(f'os valores impares são: {sorted(num[1])}')