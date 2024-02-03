# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$3.27

r = float(input('Qual valor você tem: R$'))
d = r / 3.27
print('Com o valor de R${:.2f} você consegue comprar US${:.2f}'.format(r, d))