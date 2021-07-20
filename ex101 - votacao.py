# FUNCAO
def voto(a=0):
    from datetime import date

    idade = date.today().year - a
    if idade < 16:
        print(f'com {idade} anos: NEGADO')
    elif idade >= 65 or idade < 18:
        print(f'com {idade} anos: OPCIONAL')
    else:
        print(f'com {idade} anos: OBRIGATORIO ')


# PROGRAMA PRINCIPAL

ano = int(input('ano nascimento: '))
voto(ano)
