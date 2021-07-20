import datetime

contmaior = 0
contmenor = 0
hoje = datetime.date.today().year

for c in range(1, 8, 1):
    n = int(input(f'ano de nascimento da {c}ª pessoa: '))
    idade = hoje - n
    if idade >= 18:
        contmaior += 1
    else:
        contmenor += 1

print(f'{contmaior} pessoas maiores de 18\n'
      f'{contmenor} pessoas menores de 18')
