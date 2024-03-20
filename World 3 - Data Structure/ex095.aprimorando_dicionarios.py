# Aprimore o Desafio 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador:

jogador = {}
partidas = []
time = []
while True:
    jogador.clear()
    jogador['nome'] = input('Nome do Jogador: ').capitalize()
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos gols na partida {c+1}: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? S/N ')).upper()[0]
        if resp in 'SN':
            break
        print('Valor inválido! Digite S ou N: ')
    if resp == 'N':
        break
print('-=' * 30)
print('cod', end='')
for i in jogador.keys():
    print(f'{i:>15}', end='')
print()
print('*' * 40)
for k, v in enumerate(time):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('*' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (Digite 999 para parar)'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Valor inválido! NÃo existe jogado com o código {busca}!')
    else:
        print(f'--------- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('*' * 40)
print('Volte sempre!')