matriz = [[], [], []]
num = 0
pares = 0
soma = 0
maior = 0
coluna = 0
linha = 0

for l in range(0, 3):
    for c in range(0, 3):
        num = int(input(f'digite o valor de {l, c}: '))
        matriz[l].append(num)
        if num % 2 == 0:
            pares += num

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{(matriz[l][c]):^4}]', end="")
    print()


coluna = int(input('qual coluna quer somar (1,2,3): '))
linha = int(input('qual linha quer o maior valor (1,2,3): '))


for c in range(0,3):
    soma += matriz[c][coluna-1]  # soma os numeros da coluna coluna (0,1,2)
    if matriz[linha-1][c] > maior:  # o maior valor da  linha linha
        maior = matriz[linha-1][c]

print(f'a soma de todos os pares digitados é {pares}')
print(f'o maior valor da {linha}ª linha é {maior}')
print(f'a soma dos valores da {coluna}ª coluna é {soma} ')
