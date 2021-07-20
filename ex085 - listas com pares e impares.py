lista = []
par = []
impar = []
num = 0
temp = []  #lista temporaria

for c in range(0, 7):
    num = int(input(f'digite o {c + 1}º nr: '))
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
lista.append(par[:])
lista.append(impar[:])

print(f'lista digitada {lista}')
print(f'lista de numeros pares {sorted(par)}')
print(f'lista de numeros impares {sorted(impar)}')