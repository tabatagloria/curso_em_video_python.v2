# Desenvolva um programa que leia o primeiro termo e a razão de uma progressão aritmética. No final, mostre os 10 primeiros termos dessa progressão:

t = int(input('Digite o primeiro termo da progressão aritmética: '))
r = int(input('Digite a razão da progressão aritmética: '))
p = t
for pa in range(10):
    p = t
    t += r
    print(p, end = ' ')
    