# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre: a - Quantas pessoas tem mais de 18 anos; b - Quantos homens foram cadastrados; c - Quantas mulheres tem menos de 20 anos:

total = 0
men = 0
women = 0
print('====== Cadastro de Pessoas ======')
while True:
    age = int(input('Idade: '))
    gender = ' '
    while gender not in 'FM':
        gender = input('Sexo: F/M ').upper().strip()[0]
    question = ' '
    while question not in 'SN':
        question = input('Deseja continuar cadastrando: S/N ').upper().strip()[0]
    if age >= 18:
        total += 1
    if gender == 'M':
        men += 1
    if gender == 'F' and age <= 20:
        women += 1
    if question == 'N':
        break
print(f'Foram cadastrados {total} pessoas maior(es) de 18 anos, {men} homens cadastrados e {women} mulher(es) com menos de 20 anos')