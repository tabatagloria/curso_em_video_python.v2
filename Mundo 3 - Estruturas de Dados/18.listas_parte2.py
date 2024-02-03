# Posicionamento de elementos dentro de uma lista composta:
''''pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]
print(pessoas[0][0])
print(pessoas[1][1])
print(pessoas[2][0])
print(pessoas[1])'''

''''teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
# galera.append(teste)  cria uma ligação entre as listas
galera.append(teste[:])
print(teste)
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:]) # cria uma cópia das listas
print(galera)
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera) # printa a lista completa
print(galera[0]) # printa os dados do João 
print(galera[0][0]) # printa somente o nome João
print(galera[2][1]) # printa a idade de Joaquim
for pessoa in galera:
    # print(pessoa)
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade.')'''

galera = list()
dado = list()
maior = menor = 0
for c in range(0, 3):
    dado.append(input('Nome: '))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear() # limpa a primeira lista

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        maior += 1
    else:
        print(f'{p[0]} é menor de idade')
        menor += 1
print(f'Temos {maior} maiores de idade e {menor} menores.')


