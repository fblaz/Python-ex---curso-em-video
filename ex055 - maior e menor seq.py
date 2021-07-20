lista = []

for c in range(1, 6):
    peso = int(input(f'digite o peso da {c} pessoa '))
    lista.insert(c, peso)
print(lista)
print(f'o maior peso é {max(lista)}')
print(f'o menor peso é {min(lista)}')