# FUNCOES

def ficha(jog='desconhecido', gols=0):
    """
    --> cadastra jogador e numero de gols
    :param jog: nome do jogador, OPCIONAL. Default = 'desconhecido'
    :param gols: qtdade de gols, OPCIONAL. Default = 0
    :return: nome e qtdade de gols
    """
    jog = str(input('nome do jogador: '))
    gols = input('qtdade de gols: ')
    if jog.isalpha():
        jog = jog
    else:
        jog = 'desconhecido'
    if gols.isnumeric():
        gols = gols
    else:
        gols = 0

    return f'o jogador {jog} fez {gols} gols'


# PROG PRINCIPAL

print(ficha())