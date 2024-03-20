# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade: Até 9 anos: MIRIM; Até 14 anos: INFANTIL; Até 19 anos: JUNIOR; Até 25 anos: SENIOR e acima: MASTER:

import datetime
nascimento = int(input('Digite o ano de nascimento do atleta: '))
data = datetime.date.today()
idade = data.year - nascimento
if idade <= 9:
    print('Categoria: MIRIM')
elif idade <= 14: 
    print('Categoria: INFANTIL')
elif idade <= 19:
    print('Categoria: JUNIOR')
elif idade <= 25:
    print('Categoria: SENIOR')
else:
    print('Categoria: MASTER')