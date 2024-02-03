# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela sua porção inteira. Exemplo: Digite um número: 6.127 O número 6.217 tem a parte inteira 6.

from math import trunc
num = float(input('Digite um número real: '))
t = trunc(num)
print('A porção inteira de {} é {}'.format(num, t))