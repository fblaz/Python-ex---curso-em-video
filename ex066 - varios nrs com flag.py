n = 0
cont = 0
soma = 0

while n != 999:
    soma += n
    n = int(input('digite um nr (999 para parar): '))
    if n == 999:
        break
    cont += 1
print(f'a soma dos {cont} valores é {soma}')