# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m2:

larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
area = larg * alt
print('Sua parede tem a área de {:.2}m2 e você vai precisar de {:.2f} litros de tinta.'.format(area, area / 2))
