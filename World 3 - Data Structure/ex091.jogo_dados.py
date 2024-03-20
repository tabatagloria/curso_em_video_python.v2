# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
jogo_dados = {}
cont = 0
jogo_dados['jogador1'] = randint(1,6)
jogo_dados['jogador2'] = randint(1,6)
jogo_dados['jogador3'] = randint(1,6)
jogo_dados['jogador4'] = randint(1,6)
for k, v in jogo_dados.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
print(f'{"="}'* 30)
print('RANKING DOS JOGADORES')
for i in sorted(jogo_dados, key = jogo_dados.get, reverse=True):
    cont += 1
    print(f'{cont} lugar: {i} com {jogo_dados[i]}')
    sleep(1)
print(f'{"="}'*30)


