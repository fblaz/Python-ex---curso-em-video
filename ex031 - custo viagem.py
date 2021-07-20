# FUNCOES

def passagem(dist):
    if dist < 200:
        preco = dist * 0.5
        return preco
    else:
        preco = dist * 0.45
        return preco


# PRINCIPAL

dist = float(input('qual a distancia em km? '))
print(f'para a viagem de {dist} km\n'
      f'o preco da passagem é R$ {passagem(dist):.2f}')
