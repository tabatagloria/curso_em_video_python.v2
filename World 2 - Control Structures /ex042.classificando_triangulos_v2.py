# Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado: EQUILÁTERO: todos os lados iguais; ISÓSCELES: dois lados iguais; ESCALENO: todos os lados diferentes:

r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3:
        print('Triângulo Equilátero')
    elif r1 != r2 != r3 != r1:
        print('Triângulo Escaleno')
    else: 
        print('Triângulo Isósceles')
else:
    print('Não é um triângulo')