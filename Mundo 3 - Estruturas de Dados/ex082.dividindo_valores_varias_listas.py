# Crie um programa que vai ler vários números e colocar em um lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

n = []
par = []
impar = []
q = 's'
while True:
    if q == 's':
        add = int(input('Digite um número inteiro: '))
        n.append(add)
        q = input('Desejada digitar outro valor? S/N ').lower().strip()[0]
        while q not in 'sn':
            print('Valor inválido!')
            q = input('Desejada digitar outro valor? S/N ').lower().strip()[0]
    else: 
        break        
for i in n:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)
print(f'A lista gerada foi: {n}')
print(f'Sendo os números pares: {par} e os ímpares {impar}')

