# FUNCOES

def aluguel():
    km = float(input('qtos km andou: '))
    dias = int(input('qtos dias alugou: '))
    preco = 60*dias + 0.15*km
    print(f'o valor do aluguel é de {preco:.2f} reais')


aluguel()
