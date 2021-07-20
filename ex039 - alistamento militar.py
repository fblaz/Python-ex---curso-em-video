# IMPORTAÇÕES
import datetime

# PRINCIPAL

nascimento = int(input('Informe o ano de seu nascimento: '))
idade = datetime.date.today().year - nascimento
if idade < 18:
    print(f'voce tem \033[1;31m{idade}\033[m anos, o alistamento será somente em {datetime.date.today().year + (18 - idade)}.')
elif idade == 18:
    print(f'é o ano do seu alistamento, vc tem \033[1;31m{idade}\033[m anos')
else:
    print(f'voce tem \033[1;31m{idade}\033[m anos. Já passou, seu alistamento foi em {nascimento + 18}')
