pilha = []

expressao = str(input('digite a expressão: '))

for simb in expressao:
    if simb == ('('):
        pilha.append('(')
    elif simb == (')'):
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('sua expressão foi aceita')
else:
    print('sua expressão está errada')
