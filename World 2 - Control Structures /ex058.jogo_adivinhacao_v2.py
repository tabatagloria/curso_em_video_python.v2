# Melhore o Desafio 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar. mostrando no final quantos palpites foram necessários.

from random import randint
count = 0
num_pc = randint(0, 10)
num_user = int(input('Digite um número de 0 a 10: '))
while num_pc != num_user:
    num_user = int(input('Digite um número de 0 a 10: '))
    count += 1
    if num_pc > num_user:
        print('Você errou! o número é maior que o digitado...')
    elif num_pc < num_user:
        print('Você errou! o número é menor que o digitado...')
print('O número sorteado foi {} e você precisou de {} tentativas para acertar.'.format(num_user, count))
