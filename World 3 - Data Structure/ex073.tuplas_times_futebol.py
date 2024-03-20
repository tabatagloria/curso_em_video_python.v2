# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre: a-) Apenas os 5 primeiros colocados; b-) Os últimos 4 colocados da tabela; c-) uma lista com os times em ordem alfabética; d-) Em que posição na tabela está o time da Coritiba.

teams = ('Botafogo', 'Palmeiras', 'São Paulo', 'Atlético-MG', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Fluminense', 'Fortaleza', 'Bragantino', 'Atlético-PR', 'Santos', 'Internacional', 'Corinthians', 'Cuiabá', 'Bahia', 'Goiás', 'Vasco', 'América-MG', 'Coritiba')
print(f'A lista de times do Brasileirão 2023 são: {teams}\n')
print('Os 5 primeiros colocados do campeonato brasileiro de 2023 são: ')
for t in range(0, 5):
    print(teams[t])
print('\nOs últimos 4 colocados da tabela do campeonato brasileiro de 2023 são: ')
for u in range(16,20):
    print(teams[u])
print(f'\nA lista do campeonato brasileiro 2023 em ordem alfabética é: {sorted(teams)}\n')
print('O time do Coritiba está na posição: ', teams.index('Coritiba') + 1)

