# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela. (abaixo de 7 reprovado)

aluno = {}
aluno['nome'] = input('Nome do aluno: ').capitalize()
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] < 7:
    aluno['status'] = 'Reprovado'
else:
    aluno['status'] = 'Aprovado'
for k, v in aluno.items():
    print(f'{k} é igual a {v}')