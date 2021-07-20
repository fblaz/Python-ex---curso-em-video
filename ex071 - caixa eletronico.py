# cedulas disponiveis 50, 20, 10, 1

valor = int(input('Qual o valor a ser sacado? R$ '))
cedula = 0
lista = [50, 20, 10, 1]
i = 0

while True:
    cedula = valor // lista[i]
    valor = valor % lista[i]
    if cedula > 0:
        print(f'Total de {cedula} cédulas de R$ {lista[i]}')
    i += 1
    if valor == 0:
        break
print('=' * 20)
print('Volte sempre ao Banco')
