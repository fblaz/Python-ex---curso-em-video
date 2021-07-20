dic = {}

nome = str(input('digite o nome: ')).upper()
media = float(input(f'digite a media de {nome}: '))
if media >= 7:
    status = "APROVADO"
elif 5 < media < 7:
    status = 'RECUPERAÇÃO'
else:
    status = 'REPROVADO'

dic['nome'] = nome
dic['media'] = media
dic['situação'] = status

print('=-'*20)

for k, v in dic.items():
    print(f'- {k} é igual a {v}')
