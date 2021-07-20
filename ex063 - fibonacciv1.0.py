n = int(input('quantos termos vc quer mostrar? '))
loop = 2
lista = [0, 1, 1]
fibo = 0

while loop <= n:
    loop += 1
    fibo = lista[loop-1] + lista[loop -2]
    lista.insert(loop, fibo)
print(f'{lista[:n]} - FIM')