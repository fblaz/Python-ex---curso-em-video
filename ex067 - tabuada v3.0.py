i = 0

while True:
    num1 = int(input('digite um nr '))
    if num1 < 0:
        break
    while i < 10:
        i += 1
        print(f'{num1} x {i:2} = {num1 * i}')
    print('-'*20)
    i = 0
print(f'programa finalizado')





