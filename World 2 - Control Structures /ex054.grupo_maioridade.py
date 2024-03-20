# Crie um programa que leia o ano de nascimento de 7 pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores:

from datetime import date
menores = 0
maiores = 0
date = date.today().year
for i in range(7):
    n = int(input('Digite o ano de nascimento da {} pessoa: '.format(i + 1)))
    if date - n < 18:
        menores += 1
    else:
        maiores += 1
print('Do grupo de pessoas {} são menores de idade e {} são maiores de idade.'.format(menores, maiores))

