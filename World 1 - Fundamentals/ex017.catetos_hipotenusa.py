# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa:

from math import hypot
co = float(input('Digite o valor do cateto oosto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hip = hypot(co,ca)
print('A hipotenusa do cateto oposto {} e adjacente {} é {}'.format(co, ca, hip))