# Crie um programa que faça o computador jogar JOKENPÔ com você: 

from random import choice

lista = ['Pedra', 'Papel', 'Tesoura']
pc = choice(lista)
usuario = int(input('Escolha:\n 1- Pedra\n 2 - Papel\n 3 - Tesoura\n'))
if usuario == 1:
    if pc == 'Pedra':
        print('Empate! O computador também escolheu {}.'.format(pc))
    elif pc == 'Papel':
        print('Você perdeu! Você escolheu Pedra e o computador escolheu {}.'.format(pc))
    elif pc == 'Tesoura':
        print('Você ganhou! Você escolheu Pedra e o Computador escolheu {}'.format(pc))
elif usuario == 2:
    if pc == 'Pedra':
       print('Você ganhou! Você escolheu Papel e o Computador escolheu {}'.format(pc))
    elif pc == 'Papel':
        print('Empate! O computador também escolheu {}.'.format(pc))
    elif pc == 'Tesoura':
        print('Você perdeu! Você escolheu Papel e o computador escolheu {}.'.format(pc))
elif usuario == 3:
    if pc == 'Pedra':
       print('Você perdeu! Você escolheu Tesoura e o computador escolheu {}.'.format(pc))
    elif pc == 'Papel':
        print('Você ganhou! Você escolheu Tesoura e o Computador escolheu {}'.format(pc))
    elif pc == 'Tesoura':
        print('Empate! O computador também escolheu {}.'.format(pc))
else:
    print('Jogada inválida. Tente Novamente')

    
    
