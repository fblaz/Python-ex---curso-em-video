listagem = ('APRENDER',
            'PROGRAMAR',
            'LINGUAGEM',
            'PYTHON',
            'CURSO',
            'GRATIS',
            'ESTUDAR',
            'PRATICAR',
            'TRABALHAR',
            'MERCADO',
            'PROGRAMADOR',
            'FUTURO')

for pos in range(0, len(listagem)):
    print(f'\n Na palavra {listagem[pos]}, temos as vogais: ', end=" ")
    for i in range(0, len(listagem[pos])):
        if listagem[pos].lower().strip()[i] in 'aeiou':
            print(listagem[pos].lower().strip()[i], end=' ')
