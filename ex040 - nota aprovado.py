n1 = float(input('digite a primeira nota: '))
n2 = float(input('digitea a segunda nota: '))
media = (n1+n2)/2

if media < 5:
    print(f'sua média foi {media:.2f}. REPROVADO')
elif 5 <= media < 7:
    print(f'sua média foi {media:.2f}. RECUPERAÇÃO')
else:
    print(f'sua média foi {media:.2f}. APROVADO')