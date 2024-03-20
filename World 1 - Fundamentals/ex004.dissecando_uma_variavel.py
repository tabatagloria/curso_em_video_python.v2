print('====== DESAFIO 4 ======')
# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas a informações possíveis sobre ele:

n = input('Digite algo: ')
print('Tipo primitivo: {} \nTem espaço: {} \nNúmero: {}\nAlfabético: {} \nAlfanumérico: {} \nMaúscula: {} \nMinúscula: {} \nCapitalizada: {}'.format(type(n), n.isspace(), n.isnumeric(), n.isalpha(), n.isalnum(), n.isupper(), n.islower(), n.istitle()))