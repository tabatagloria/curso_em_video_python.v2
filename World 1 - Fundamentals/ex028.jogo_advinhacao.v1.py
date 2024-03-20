# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint

num_pc = randint(0, 5)
num_user = int(input('Digite um número de 0 a 5: '))
if num_user > num_pc:
    print('Você digitou um número inválido!')
else: 
    if num_pc == num_user:
        print('Você venceu!')
    else:
        print('Você perdeu! Você digitou {} e o número era {}'.format(num_user, num_pc))