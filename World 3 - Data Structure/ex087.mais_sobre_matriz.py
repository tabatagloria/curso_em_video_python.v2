# Aprimore o desafio anterior, mostrando no final: a-) A soma de todos os valores pares digitados; b-) A soma dos valores da terceira coluna; c-) O maior valor da segunda linha:

matriz = []
l1 = []
l2 = []
l3 = []
pares = soma = 0
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
for i in matriz:
    for n in i:
        if n % 2 == 0:
            pares += n
print(f'Sendo a soma dos valores pares: {pares}')
soma = matriz[0][2] + matriz[1][2] + matriz[2][2]
print(f'Sendo a soma da terceira coluna {soma}')
print(f'E o maior valor da segunda linha é {max(matriz[1])}')

