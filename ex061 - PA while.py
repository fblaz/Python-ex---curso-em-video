print('GERADOR DE PA')
print('=-'*20)
termo = int(input('digite o primeiro termo '))
razao = int(input('digite a razao '))
cont = 1

while cont <= 10:
    print(f'{termo} - ', end='')
    termo += razao
    cont += 1
print('FIM')
