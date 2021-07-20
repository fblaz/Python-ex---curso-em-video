boletim = []
media = 0
n1 = 0
n2 = 0
nome = 0
p = 0

while True:
    nome = str(input('nome: ')).upper()
    n1 = float(input('nota 1: '))
    n2 = float(input('nota 2: '))
    media = (n1+n2)/2
    # boletim.append([nome, [n1, n2], media]) também funciona usando append
    boletim.insert(p, [nome, [n1, n2], media])
    p += 1
    loop = ' '
    while loop not in 'SN':
        loop = str(input('QUER CONTINUAR? [S/N] ')).upper().strip()[0]
    if loop == 'N':
        break

print(f'{"No":<4}', f'{"ALUNO":<10}', f'{"MEDIA":<4}')
#  print(f'{"No.":<4}{"NOME":<4}{"MEDIA":<4}')
print('-'*40)

for i, a in enumerate(boletim):
    print(f'{i:<4} {a[0]:<10} {a[2]:<4.1f}')
print('-'*40)

while True:
    resp = ' '
    while resp not in range(0, len(boletim)) and resp != 999:
        resp = int(input('mostrar a nota de qual aluno? (999 interrompe): '))
    if resp == 999:
        print('FINALIZANDO...')
        print('<<< VOLTE SEMPRE >>>')
        break
    else:
        print(f'notas de {boletim[resp][0]} foram: {boletim[resp][1]}')
        print('='*40)
