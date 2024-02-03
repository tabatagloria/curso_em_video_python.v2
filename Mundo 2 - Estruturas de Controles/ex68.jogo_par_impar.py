# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo:

from random import randint
print('====== PAR OU ÍMPAR =====')

result = 0
count = 0
while True:
    num_pc = randint(0, 10)
    num_user = int(input('Digite um número inteiro de 0 a 10: '))
    result = num_pc + num_user
    choice = ' '
    while choice not in 'PI':
        choice = str(input('Digite P para par ou I para impar: ')).upper().strip()[0]
    print('Deu PAR' if result % 2 == 0 else 'Deu ÍMPAR')
    if choice == 'P' and result % 2 == 0: 
        count += 1
        print(f'Você ganhou! Total {result}, você escolheu o {num_user} e o computador {num_pc}.')
    elif choice == 'I' and result % 2 != 0:
        count += 1
        print(f'Você ganhou! Total {result}, você escolheu o {num_user} e o computador {num_pc}.')
    else:
        print(f'Você perdeu! Total {result}, você escolheu o {num_user} e o computador {num_pc}.')
        break
print(f'Fim do Jogo! Você teve o total de {count} vitória(s).')