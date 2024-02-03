# Crie um programa que crie uma matriz 3x3 e preencha os com valores lidos pelo teclado. No final mostre a matriz na tela, com a formatação correta:

matriz = []
l1 = []
l2 = []
l3 = []
for n1 in range(3):
    l1.append(int(input(f'Digite o {n1+1} número da primeira linha: ')))
for n2 in range(3):
    l2.append(int(input(f'Digite o {n2+1} número da segunda linha: ')))
for n3 in range(3):
    l3.append(int(input(f'Digite o {n3+1} número da terceira linha: ')))
matriz.append(l1[:])
matriz.append(l2[:])
matriz.append(l3[:])
print(matriz[0])
print(matriz[1])
print(matriz[2])