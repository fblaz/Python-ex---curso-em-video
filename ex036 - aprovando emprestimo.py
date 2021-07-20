casa = float(input('qual o valor da casa? '))
sal = float(input('qual o salario? '))
anos = float(input('em quantos anos vai pagar? '))
mensalidade = casa/(anos*12)

if mensalidade < sal * 0.30:
    print(f'\033[1;32mEMPRESTIMO APROVADO!\033[m\n'
          f'o valor da mensalidade será {mensalidade:.2f} reais')
else:
    print(f'\033[1;31mEMPRESTIMO NEGADO!\033[m\n'
          f'o salario mínimo deverá ser de {(mensalidade/0.3):.2f} reais')