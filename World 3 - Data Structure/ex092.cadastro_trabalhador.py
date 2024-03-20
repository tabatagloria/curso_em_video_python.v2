# Crie um programa que leia nome, ano de nascimento e a carteira de trabalho e cadastre-os (com idade) em um dionário se por acaso a CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar (após 35 anos de contribuição):

from datetime import date
today = date.today()
trabalhador = {}
trabalhador['nome'] = input('Nome do trabalhador: ').capitalize()
nasc = int(input('Ano de nascimento: '))
trabalhador['idade'] = today.year - nasc
trabalhador['ctps'] = int(input('Carteira de trabalho (digite 0 caso não tenha): '))
if trabalhador['ctps'] == 0:
    print(f'{"="}' * 30)
    for k, v in trabalhador.items():
        print(f'- {k} tem o valor de {v}')
    print(f'{"="}' * 30)
else:
    trabalhador['contratação'] = int(input('Ano de contratação: '))
    trabalhador['salário'] = float(input('Salário: '))
    trabalhador['aposentadoria'] = trabalhador['contratação'] + 35
    print(f'{"="}' * 30)
    for k, v in trabalhador.items():
        print(f'- {k} tem o valor de {v}')
    print(f'{"="}' * 30)