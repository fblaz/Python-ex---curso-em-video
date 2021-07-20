preco = float(input('digite o preço das compras: '))
desc = [0.9, 0.95, 1, 1.2]

print(f'FORMAS DE PAGAMENTO: \n'
      f'{"[ 0 ] À VISTA DINHEIRO / CHEQUE"}\n'
      f'{"[ 1 ] À VISTA CARTÃO"}\n'
      f'{"[ 2 ] 2 X CARTÃO"}\n'
      f'{"[ 3 ] 3 X OU MAIS NO CARTÃO"}\n')
opc = 4
while opc > 3:
    opc = int(input('qual a opção? '))

valor = preco * desc[opc]

if opc == 0 or opc == 1:
    print(f'sua compra de R$ {preco:.2f}, com desconto, será de R$ {valor:.2f}')
elif opc == 2:
    print(f'sua compra de R$ {preco:.2f}, com desconto, será de:\n'
          f'2 parcelas de R$ {(valor/2):.2f}')
else:
    parc = int(input('digite em quantas parcelas: '))
    print(f'sua compra de R$ {preco}, com desconto, será de:\n'
          f'{parc} parcelas de R$ {valor/parc}')
