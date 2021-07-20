n = 0
cont = 0
acumulador = 0

while n != 999:
    acumulador += n
    cont += 1
    n = int(input('digite um nr ou 999 para parar: '))
print(f'voce digitou {cont-1} e a soma deles é {acumulador}')
