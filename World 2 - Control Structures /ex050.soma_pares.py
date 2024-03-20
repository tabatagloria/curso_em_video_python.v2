# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o:

soma = 0
cont = 0

for x in range(1, 7):
    n = int(input('Digite o {} valor: '.format(x)))
    if n % 2 == 0:
        soma += n
        cont += 1
print('A soma dos {} números pares digitados é: {}'.format(cont, soma))

