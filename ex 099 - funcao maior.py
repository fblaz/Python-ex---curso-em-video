def maior(lista):
    print(f'foram informados {len(lista)} valores')
    print(f'o maior valor é {max(lista)}')

# PRINCIPAL
lista = []

while True:
    valores = int(input('valores: '))
    lista.append(valores)
    while True:
        resp = str(input('quer continuar: [S/N]')).upper()[0]
        if resp in 'SN':
            break
    if resp == 'N':
        break

maior(lista)