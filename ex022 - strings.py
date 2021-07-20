nome = input('digite seu nome completo: ').strip()
print(f'NOME = {nome.upper()}\n'
      f'nome = {nome.lower()}\n'
      f'o nome tem {len(nome) - nome.count(" ")} letras \n'
      f'o primeiro nome tem {nome.find(" ")} \n')