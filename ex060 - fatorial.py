n = int(input('digite um nr: '))
c = n
i = 1
f = 1
while c > 0:
    print(f'{c}', end="")
    print(f' x ' if c > 1 else f' = {f}', end="")
    f = f * c
    c -= 1