# FUNCAO

def fatorial(num=1, show=False):
    """
    --> calcula o fatorial do numero
    :param num: numero a ser calculado
    :param show: (opcional) mostra ou não a conta
    :return: o valor do fatorial de um nr n
   """

    fat = 1
    for n in range(num, 0, -1):
        fat *= n
        if show:
            print(f'{n:2}', 'x' if n > 1 else'= ', end="")
    return fat


# PROGRAMA PRINCIPAL

print(fatorial(4, show=True))
help(fatorial)