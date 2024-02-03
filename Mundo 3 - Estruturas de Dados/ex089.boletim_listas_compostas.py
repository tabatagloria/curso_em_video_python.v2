# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente:
alunos = []
boletim = []
notas = []
p = 's'
media = 0
c = ''
aluno = ''
while True:
    if p == 's':
        nome = input('Digite o nome do aluno: ').title()
        for n in range(2):
            notas.append(float(input(f'Digite a nota {n+1}: ')))
        alunos.append(nome)
        alunos.append(notas[:])
        notas.clear()
        boletim.append(alunos[:])
        alunos.clear()
        p = input('Deseja cadastrar outro aluno? S/N ').lower().strip()[0]
        while p not in 'sn':
            print('Valor inválido!')
            p = input('Deseja cadastrar outro aluno? S/N ').lower().strip()[0]
    else:
        break
print('-' * 40)
print(f'{"BOLETIM":^40}')
print('-' * 40)
print(f'{"NOME DO ALUNO":^20}', end='')
print(f'{"MÉDIA":^20}')
print('-' * 40)
for i in boletim:
    print(f'{i[0]:.<35}', end = '')
    media = (i[1][0] + i[1][1]) / 2
    print(f'{media}')
    media = 0
print('-'*40)
while True:
    c = input('Deseja ver as notas de um aluno? S/N ').lower().strip()[0]
    while c not in 'sn':
        print('Valor inválido!')
        c = input('Deseja ver as notas de um aluno? S/N ').lower().strip()[0]
    if c in 'Ss':
        aluno = input('Nome do aluno: ').title().strip()
        for a in boletim:
            if aluno in a:
                print(f'As notas de {aluno} são: ')
                print(a[1])
    else:
        break
print('Fim do programa!')


