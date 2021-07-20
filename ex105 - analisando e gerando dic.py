# FUNCAO

def notas(*n, sit=False):
    """
    --> recebe as notas e grava em um dicionario
    :param n: notas
    :param sit: Opcional de mostrar ou não a situação
    :return: retrona um dicionario
    """
    lista = [*n]
    dic = {'total': len(lista), 'maior': max(lista), 'menor': min(lista), 'média': sum(lista) / len(lista)}
    if sit == True:
        if dic['média'] >= 6 and dic['média'] <= 8:
            dic['sit'] = 'RAZOAVEL'
        elif dic['média'] >= 8:
            dic['sit'] = 'BOA'
        else:
            dic['sit'] = 'RUIM'
    return dic


# PROGRAMA PRINCIPAL

resp = notas(5.5, 2, 1.5, sit=True)
print(resp)
help(notas)
