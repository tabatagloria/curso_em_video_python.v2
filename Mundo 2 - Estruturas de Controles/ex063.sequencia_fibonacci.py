# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci. Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
print('Sequência de Fibonacci:\n')
n = int(input('Digite um número: '))
count = 3
t1 = 0
t2 = 1
f = 1
print('{} -> {}'.format(t1,t2), end = ' -> ')
while count <= n:
    f = t1 + t2
    print(f, end = ' -> ')
    t1 = t2
    t2 = f
    count += 1
print('Fim')
    