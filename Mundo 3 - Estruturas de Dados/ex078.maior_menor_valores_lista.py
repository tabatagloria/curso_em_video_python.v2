# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posiçoes na lista.
n = []
for i in range(1, 6):
    q = int(input(f'Digite o {i} número: '))
    n.append(q)
print(f'O maior valor digitado foi {max(n)} que está na posição {n.index(max(n))}')
print(f'O menor valor digitado foi {min(n)} que está na posição {n.index(min(n))}')
