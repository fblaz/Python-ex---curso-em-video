print('GERADOR DE PA')
print('=-'*20)
termo = int(input('digite o primeiro termo: '))
razao = int(input('digite a razao: '))
cont = 1
loop = 10
total = 0

while loop != 0:
    total = total + loop
    while cont <= total:
        print(f'{termo} - ', end="")
        termo += razao
        cont += 1
    print('PAUSA')
    loop = int(input('Quantos termos voce quer mostrar a mais? '))
print(f'Progressão finalizada com {cont -1} termos mostrados')
