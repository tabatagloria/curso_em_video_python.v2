# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: a -) Quantas pessoas foram cadastradas; b -) A média de idade do grupo; c -) Uma lista com todas as mulheres; d -) Uma lista com todas as pessoas com idade acima da média:

pessoas = {}
cadastro = []
mulheres = []
pergunta = 's'
media = 0
m = 0
while True:
    if pergunta == 's':
        pessoas['nome'] = input('Nome: ').capitalize()
        s = input('Sexo: F/M ').lower().strip()[0]
        while s not in 'fm':
            print('Valor inválido!')
            s = input('Sexo: F/M ').lower().strip()[0]
        pessoas['sexo'] = s
        if s == 'f':
            mulheres.append(pessoas['nome'])
        pessoas['idade'] = int(input('Idade: '))
        m = m + pessoas['idade']
        pergunta = input('Quer continuar? S/N ').lower().strip()[0]
        while pergunta not in 'sn':
            print('Valor inválido!')
            pergunta = input('Quer continuar? S/N ').lower().strip()[0]
        cadastro.append(pessoas.copy())
    else:
        break
print(f'{"-=" * 30}')
total = len(cadastro)
media = m / total
print(f'A) Temos o total de {total} pessoas cadastradas.')
print(f'B) A média e idade do grupo é de {media}.')
print(f'C) As mulheres do grupo são: {mulheres}')
print('A lista de pessoas com idade acima da média são: ')
for e in cadastro:
    for k, v in e.items():
        if k == 'idade' and v > media:
                print(e)

     




