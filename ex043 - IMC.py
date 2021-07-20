# FUNCOES

def imc (pes, alt):
    imc = peso/(alt**2)
    return imc


# Principal

peso = float(input('digite o seu peso em kg: '))
altura = float(input('digite a sua altura em metros: '))
imc = imc(peso, altura)

if imc < 18.5:
    print(f'abaixo do peso. IMC = {imc:.2f}')
elif 18.5 <= imc < 25:
    print(f'peso ideal. IMC = {imc:.2f}')
elif 25 <= imc < 30:
    print(F'sobrepeso. IMC = {imc:.2f}')
elif 30 <= imc < 40:
    print(f'obesidade. IMC = {imc:.2f}')
else:
    print(f'obesidade morbida. IMC = {imc:.2f}')