x = float(input('digite o segmento 1: '))
y = float(input('digite o segmento 2: '))
z = float(input('digite o segmento 3: '))

if x < y + z and y < x + z and z < x + y:
    print(f'os segmentos {x, y, z} formam um Triangulo')
else:
    print(f'os segmentos {x, y, z} NÃO formam um Triangulo')
