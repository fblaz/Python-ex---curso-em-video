numeros = []

for c in range(0, 5):
    num = int(input(f'digite o {c + 1}º nr: '))
    d = 0
    if c == 0:
        numeros.insert(c, num)
    elif num > numeros[c-1]:
        while num > numeros[c-1] and (c-1) <= len(numeros):
            c += 1
            d = c
            if (c - 1) == len(numeros):
                break
        numeros.insert(d, num)
    elif num < numeros[c-1]:
        while num < numeros[c-1] and (c-1) >= 0:
            c -= 1
            d = c
            if (c - 1) < 0:
                break
        numeros.insert(d, num)
    else:
        numeros.insert(c, num)

print(numeros)
