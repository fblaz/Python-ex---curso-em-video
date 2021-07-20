import math

# PRINCIPAL

a, b, c = input('digite 3 valores: ').split()
n1 = float(a)
n2 = float(b)
n3 = float(c)
lista = [n1, n2, n3]
print(lista)
x = min(lista)
y = max(lista)
print(f'o maior valor é {y}')
print(f'o menor valor é {x}')


