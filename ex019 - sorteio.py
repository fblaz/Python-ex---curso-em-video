import random

a, b, c, d = input('digite o nome de 4 alunos: ').split()
lista = [a, b, c, d]
escolhido = random.choice(lista)
print(f'o aluno escolhido foi {escolhido}')


