# Crie um programa onde o usuário possa digitar valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

n = []
q = 's'
while True:
    if q == 's':
        add = int(input('Digite um valor: '))
        if add not in n:
            n.append(add)
            print('Valor adicionado com sucesso!')
        else:
            print('Valor já existe na lista, não cadastrado!')
        q = input('Deseja digitar outro valor: S/N ').lower().strip()[0]
        while q not in 'sn':
            print('Valor inválido!')
            q = input('Deseja digitar outro valor: S/N ').lower().strip()[0]          
    else:
        break        
print(f'Os valores cadastrados na lista foram: {n}')
