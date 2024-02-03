# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre: a-) quantas vezes apareceu o valor 9; b-) em que posição foi digitado o primeiro valor 3; c-) quais foram os números pares.

cont = 0
n = tuple(int(input(f'Digite um número: ')) for i in range(0,4)) 
print(f'O número 9 apareceu {n.count(9)} vez(es).')
if 3 in n:
    print(f'O número 3 apareceu na posição {n.index(3)+1}')
else:
    print('O número 3 não foi digitado nenhuma vez')
print('Foram digitados os seguintes números pares: ', end = '')
for i in n:
    if i % 2 == 0:
     print(f'{i}', end = ' ')