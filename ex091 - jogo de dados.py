from random import randint
from time import sleep
import operator


dic = {}
lista = []

for i in range(0, 4):
    dic[f'jogador{i+1}'] = randint(1, 6)

for k, v in dic.items():
    print(f'o {k} tirou {v} no dado.')
    sleep(0.5)


# sorteddic = sorted(dic.items(), key=operator.itemgetter(1))   # itemgetter(1) para valor e 0 para chave

sorteddic = sorted(dic.items(), key=lambda x: x[1], reverse=True)

# devolve uma lista de pares de valores chave do dicionário e o tipo de dados do seu elemento é tuple.
# O x é o elemento deste tuple, onde x[0] é a chave e x[1] é o valor.
# key=lambda x:x[1] indica que a chave de comparação é o valor dos elementos do dicionário.
# O parâmetro opcional reverse poderia ser definido para ser True se os valores precisarem
# ser ordenados em ordem decrescente.

print('=-'*30)
print('RANKING DOS JOGADORES')

for i, v in enumerate(sorteddic):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')



