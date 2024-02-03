# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

n = []
for i in range(5):
    num = int(input(f'Digite {i+1} número inteiro: '))
    for chave, valor in enumerate(n):
        if num < valor:
            n.insert(chave, num)
            break
    else:
        n.append(num)
print("Lista atual:", n)
