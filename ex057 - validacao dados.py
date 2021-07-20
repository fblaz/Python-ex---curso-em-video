sexo = str(input('Informe seu sexo [M / F]: ')).strip().upper()[0] # pega somente a primeira letra

while sexo != 'M' and sexo != 'F':
    sexo = str(input('DADOS INVALIDOS. Informe seu sexo [M / F]: ')).strip().upper()

