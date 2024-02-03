# Dicionários = variáveis compostas, é possível nomear os índices

# Declaração:
# dados = dict() ou dados = {}
# print(variável.values()) = retorna os valores contidos nos diciários
# print(variável.keys()) = retorna os índices
# print(variável.items()) = retorna os valores e os índices
# del pessoas['sexo]

pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas)
print(pessoas['nome'])
pessoas['nome'] = 'Leandro' # altera a chave nome
pessoas['peso'] = 98.5 # adiciona um elemento novo no dicinário
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k in pessoas.keys():
    print(k)
for v in pessoas.values():
    print(v)
for k, v in pessoas.items():
    print(f'{k} = {v}')

# dicionário dentro de uma lista:
estado1 = {'UF': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'UF': 'São Paulo', 'sigla': 'SP'}
brasil = []
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0])
print(brasil[0]['UF'])

estado = {}
brasil = []
for c in range(0,3):
    estado['uf'] = input('Unidade Federativa: ')
    estado['sigla'] = input('Sigla do Estado: ')
    brasil.append(estado.copy()) # método para coiar um dicionário
print(brasil)
for e in brasil:
    print(e)
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')