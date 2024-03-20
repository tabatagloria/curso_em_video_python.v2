# Faça um programa que tenha uma função chamada area(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno:

def area(largura, comprimento):
    t = largura * comprimento
    print(f'A área do terreno é {t:.2f} metros quadrados.')

a = float(input('Digite a largura do terreno: '))
b = float(input('Digite o comprimento do terreno: '))
area(a, b)
 

