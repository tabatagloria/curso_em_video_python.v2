# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seu seno, cosseno e tangente desse ângulo:

from math import sin, cos, tan, radians

angulo = float(input('Digite o valor do ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('Para o ângulo {} temos o seno {:.2f}, cosseno {:.2f} e tangente {:.2f}'.format(angulo, seno, cosseno, tangente))