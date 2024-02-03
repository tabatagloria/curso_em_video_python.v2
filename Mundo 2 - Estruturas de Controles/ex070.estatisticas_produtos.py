# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre: a - Qual é o total gasto na compra; b - Quantos produtos custam mais de R$1000,00; c - Qual é o nome do produto mais barato:

price = 0
total = 0
c = 0
cheap = ''
expensive = 0
count = 0
print('===== Cadastro de Produtos ======')
while True:
    name = input('Nome do produto: ')
    price = float(input('Preço do produto: R$'))
    count += 1
    total = total + price
    question = ' '
    while question not in 'SN':
        question = input('Deseja continuar: S/N ').upper().strip()[0]
    if question == 'N':
        break
    if price > 1000.00:
        expensive += 1
    if count == 1 or price < c:
        c = price
        cheap = name      
print(f'O total da compra foi R${total:.2f}, sendo que {expensive} produto(s) custaram mais de R$1000,00 e {cheap} é o nome do produto mais barato.')
    


