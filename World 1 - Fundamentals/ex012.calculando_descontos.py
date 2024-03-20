# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto:

p = float(input('Preço do produto: R$'))
d = p - (p * 0.05)
print('O preço final com o desconto de 5% é R${:.2f}'.format(d))