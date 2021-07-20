listagem = ('lapis', 1.75,
            'borracha', 2.00,
            'caderno', 1.75,
            'estojo', 25,
            'transferidor', 4.20,
            'compasso', 9.99,
            'mochila', 120.32,
            'canetas', 22.30,
            'livro', 34.90)
print('-'*40)
print(f'{"LISTAGEM DE PREÇO":^40}')
print('-'*40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:  #posicao pares são os nomes
        print(f'{listagem[pos]:.<30}', end ="") # < alinha a esquerda com 30 caracteres preenchidos por .
    else:
        print(f'R$ {listagem[pos]:>6.2f}')

print('-'*40)