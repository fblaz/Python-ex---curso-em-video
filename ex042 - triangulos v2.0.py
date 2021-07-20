n1, n2, n3 = input('digite os segmentos do triangulo: ').split()
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)
lista = [n1, n2, n3]

if n1 > n2 + n3 or n2 > n1 + n3 or n3 > n2 + n1:
    print(f'{lista} não formam um triangulo')
elif n1 == n2 == n3:
    print(f'{lista} formam um triangulo Equilatero')
elif n1 != n2 != n3 != n1:
    print(f'{lista} formam um triangulo escaleno')
else:
    print(f'{lista} formam um triangulo isosceles')