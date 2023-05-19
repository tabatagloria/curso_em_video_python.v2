# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo:

from random import randint
print('====== PAR OU ÍMPAR =====')
num_pc = 0
num_user = 0
result = 0
count = 0
while True:
    num_pc = randint(0, 10)
    choise = input('Digite P para par ou I para impar: ').upper().strip()
    num_user = int(input('Digite um número inteiro de 0 a 10: '))
    result = num_pc + num_user
    if choise == 'P' and result % 2 == 0: 
        count += 1
        print(f'Você ganhou! Você escolheu o {num_user} e o computador {num_pc}.')
    elif choise == 'I' and result % 2 != 0:
        count += 1
        print(f'Você ganhou! Você escolheu o {num_user} e o computador {num_pc}.')
    else:
        break
print(f'Fim do Jogo! Você teve o total de {count} vitória(s).')