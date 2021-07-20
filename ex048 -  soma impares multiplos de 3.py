contador = 0
acumulador = 0

for c in range(3, 501, 3):
    if c % 2 != 0:
        acumulador += c
        contador += 1

print(f'a soma dos \033[1;33m{contador}\033[m multiplos de 3 entre 1 e 500 é \033[1;31m{acumulador}\033[m')