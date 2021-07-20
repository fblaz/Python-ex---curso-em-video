frase = str(input('digite a frase ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for c in range(len(junto)-1, -1, -1):
    inverso += junto[c]

if junto == inverso:
    print(f'{junto} é palindromo \n'
          f'{junto} = {inverso}')
else:
    print(f'{junto} não é palindromo\n'
          f'{junto} != {inverso}')
