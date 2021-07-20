print('='*20)
print(f'{"10 TERMOS DE UMA PA"}')
print("="*20)

termo = int(input('digite o primeiro termo: '))
razao = int(input('digite a razao: '))

for c in range(termo, (termo + razao*10), razao):
    print(f'{c}', end=" - ")
print('acabou')