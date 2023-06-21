n = []
for i in range(5):
    num = int(input('Digite um número inteiro: '))
    for chave, valor in enumerate(n):
        if num < valor:
            n.insert(chave, num)
            break
    else:
        n.append(num)
print(n)