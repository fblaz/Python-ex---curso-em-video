# FUNCAO
def leiaint(num):
    """
    --> programa só vai retornar se o numero for inteiro
    :param num: recebe o numero digitado
    :return: numero
    """

    while True:
        try:
            num = int(input('digite um nr: '))
            break
        except ValueError:
            print('ERRO! DIGITE UM NR INTEIRO')
    return num


# PROGRAMA PRINCIPAL
n = leiaint('digite um nr: ')
print(f'voce acabou de digitar o nr {n}')
