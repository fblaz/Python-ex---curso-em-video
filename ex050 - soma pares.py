contador = 0
acumulador = 0

for c in range(1, 7, 1):
    x = int(input('digite um nr: '))
    if x % 2 == 0:
        contador += 1
        acumulador += c

print(f'{contador} numeros pares digitados\n'
      f'{acumulador} a soma deles')