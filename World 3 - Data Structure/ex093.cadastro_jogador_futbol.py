# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato:
jogador = {}
jogos = []
cont = 0
c = 1
jogador['nome'] = input('Nome do Jogador: ').capitalize()
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
for i in range(partidas):
    p = int(input(f'Quantos gols na partida {i+1}: '))
    jogos.append(p)
    cont = cont + p
jogador['gols'] = jogos
jogador['total'] = cont
print(f'{"="}' * 30)
print(jogador)
print(f'{"="}' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print(f'{"="}' * 30)
print(f'O jogador {jogador["nome"]} jogou {partidas}.')
for i in jogador['gols']:
    print(f'Na partida {c}, fez {i} gols.')
    c += 1
print(f'foi um total de {jogador["total"]}')
print(f'{"="}' * 30)
