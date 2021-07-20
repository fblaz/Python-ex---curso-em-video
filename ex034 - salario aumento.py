# FUNCOES

def aumento(salario):
    if salario > 1250:
        novosal = salario * 1.1
        print(f'seu antigo salario é de {salario}\n'
              f'o novo salario é {novosal:.2f} reais')
    else:
        novosal = salario * 1.15
        print(f'seu antigo salario é de {salario}\n'
              f'o novo salario é {novosal:.2f} reais')


# PRINCIPAL

salario = float(input('digite o seu salario? '))
aumento(salario)
