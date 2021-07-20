import datetime

cadastro = dict()
cadastro['nome'] = str(input('nome: '))
cadastro['ano nascimento'] = int(input('ano nascimento: '))
cadastro['ctps'] = int(input('carteira de trabalho (0 não tem): '))
if cadastro['ctps'] == 0:
    for k, v in cadastro.items():
        print(f'{k} tem o valor {v}')
else:
    cadastro['contratacao'] = int(input('ano de contratacao: '))
    cadastro['salario'] = float(input('salario: '))
    cadastro['aposentadoria'] = 40 - (datetime.date.today().year - cadastro['contrato'])
    for k, v in cadastro.items():
        print(f'{k} tem o valor {v}')