# Tuplas são imutáveis
lanche = ('hamburguer', 'suco', 'pizza', 'pudim', 'batata frita')
print(lanche)
print(lanche[1])
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(len(lanche))
for i in lanche:
    print(f'Eu vou comer {i}')

#Quando precisar imprimir a posição além do índice:
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi pra caramba!')

# printa em ordem alfabética
print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
print(c.count(5))
print(c.index(8))

# Tuplas aceitam em Python tipos de variáveis diferentes:
pessoa = ('Gustavo', 39, 'M', 99.88)
print(pessoa)
del(pessoa) # deleta os dados da tupla


