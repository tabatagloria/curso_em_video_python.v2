# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)

n = 0
count = 0
soma = 0
n = int(input('Digite um número para somar, sendo 999 a condição de parada do programa: '))
while n != 999:
    count += 1
    soma += n
    n = int(input('Digite um número para somar, sendo 999 a condição de parada do programa: '))
print('Foram digitados o total de {} números. A soma dos números foi {}'.format(count, soma))
print('Fim do programa!')
