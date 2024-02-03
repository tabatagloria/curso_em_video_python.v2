# Refaça o exercício 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for:

n = int(input('Digite um número inteiro: '))
mult = 0
print('=' * 20)
print('A tabuada do número {} é:'.format(n))
for x in range(0, 11):
    print('{} x {:2} = {:2}'.format(n, x, x * n))
print('=' * 20)