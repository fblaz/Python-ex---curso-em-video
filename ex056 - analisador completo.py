lista = []
soma_idade = 0  # media das idades no final
velho = 0  # homem mais velho
meninas = 0  # mulher menor de 20 anos

for c in range(0, 4):
    print(f'---- {c + 1}ª PESSOA ----')
    nome = str(input('digite o nome: ')).upper()
    idade = int(input('digite a idade: '))
    sexo = str(input('digite o sexo F/M: ')).upper()
    soma_idade += idade
    lista.insert(c, (nome, idade, sexo))

for c in range(0, len(lista)):
    sexolista = lista[c][2]
    idadelista = lista[c][1]
    pessoalista = lista[c][0]
    if sexolista == 'M' and idadelista > velho:
        velho = idadelista
        pessoa = pessoalista

    if sexolista == 'F' and idadelista < 20:
        meninas += 1

print(f'A média de idade do grupo é de {soma_idade / len(lista)} anos')
print(f'O homem mais velho é {pessoa} com {velho} anos')
print(f'Ao todo são {meninas} mulheres menores de 20 anos')