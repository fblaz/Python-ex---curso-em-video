# IMPORTACOES
import random


# FUNCOES

def sorteia(x):
    lista = []
    for i in range(0, x):
        num = random.randint(0, 100)
        lista.append(num)
    print(lista)
    return lista


def somapar(lista):
    pares = []
    for x in lista:
        if x % 2 == 0:
            pares.append(x)
    print(pares)
    print(f'a soma dos pares é {sum(pares)} ')


# PRINCIPAL

y = sorteia(5)
somapar(y)
