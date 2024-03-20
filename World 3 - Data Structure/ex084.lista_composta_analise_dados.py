# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:  a-) Quantas pessoas foram cadastradas; b-) Uma listagem com as pessoas mais pesadas; c-) Uma listagem com as pessoas mais leves:

dados = []
pessoas = []
cont = 's'
p = l = 0
while True:
    if cont == 's':
        dados.append(input('Nome: ').title())
        dados.append(float(input('Peso: ')))
        pessoas.append(dados[:])
        dados.clear()
        cont = input('Deseja continuar cadastrando? S/N ').lower().strip()[0]
        while cont not in 'sn':
            print('Valor inválido!')
            cont = input('Deseja continuar cadastrando? S/N ').lower().strip()[0]
    else:
        break
print(f'Foram cadastradas {len(pessoas)} pessoas')
for n in range(len(pessoas)):
    if n == 0:
        p = l = pessoas[0][1]
    else:
        if pessoas[n][1] > p:
            p = pessoas[n][1]
        if pessoas[n][1] < l:
            l = pessoas[n][1]
print('A(s) pessoa(s) mais pesada(s) são: ', end='')
for i, v in enumerate(pessoas):
    if v[1] == p:
        print(f' {v[0]}', end='')
print(f' com {p:.2f} quilos')
print('A(s) pessoa(s) mais leve(s) são: ', end='')
for i, v in enumerate(pessoas):
    if v[1] == l:
        print(f'{v[0]}', end='')
print(f' com {l:.2f} quilos')



        

    



#print(f'Sendo a(s) mais pesada(s) {max(pessoas)} e {min(pessoas)} a(s) mais leves.')




