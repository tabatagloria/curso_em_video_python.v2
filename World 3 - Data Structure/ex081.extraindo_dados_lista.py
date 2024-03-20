# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre: a - quantos números foram digitados; b - a lista de valores, ordenada de forma decrescente; c - se o valor 5 foi digitado e está ou não na lista.
n = []
q = 's'
while True:
    if q == 's':
        add = int(input('Digite um valor: '))
        n.append(add)
        q = input('Deseja digitar outro valor: S/N ').lower().strip()[0]
        while q not in 'sn':
            print('Valor inválido!')
            q = input('Deseja digitar outro valor: S/N ').lower().strip()[0]
    else:
        break
print(f'Foram cadastrados {len(n)} números na lista sendo eles: {n}')
n.sort(reverse=True)
print(f'A lista ordenada de forma decrescente é: {n}')
if 5 in n:
    print('O número 5 foi adicionado na lista')
else:
    print('O número 5 não foi adicionado a lista')
