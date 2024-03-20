# Faça um programa que ajude um jogador da Mega Sena a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em um lista composta:
from time import sleep
from random import randint
megasena = []
palpites = []
total = 1
n = 0
jogos = int(input('Quantos palpites para a Mega Sena deseja sortear: '))
while total <= jogos:
    cont = 0
    while True:
        n = randint(1, 60)
        if n not in palpites:
            palpites.append(n)    
            cont += 1
        if cont >= 6:
            break
    palpites.sort()
    megasena.append(palpites[:])
    palpites.clear()
    total += 1
print('Os números escolhidos foram: ')
for i, l in enumerate(megasena):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
