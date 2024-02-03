# Listas são mutáveis

# Declaração de listas:
num = [2, 5, 9, 1]
print(num)
# modificando uma lista:
num[2] = 3
print(num)

# para adicionar um elemento no final da lista:
num.append(7)
print(num)

# para coloca a lista em ordem crescente:
num.sort()
print(num)

# para coloca a lista em ordem decrescente:
num.sort(reverse=True)
print(num)

# para saber a quantidade de elementos tem na lista:
print(f'Essa lista tem {len(num)} elementos')

# para adicionar valores em uma posição específica:
num.insert(2, 0) # posição aonde deseja incluir o valor e o valor que deseja inserir
print(num)

# para remover um valor de uma lista:
num.pop() # sem parâmetro ele remove o último elemento da lista
print(num)
num.pop(2) # com o parâmetro remove sa posição indicada
print(num)

# para remover a primeira ocorrência de um valor:
num.insert(2, 2)
num.remove(2)
print(num)

if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')

valores = list() # outra maneira de declarar uma lista
valores.append(5)
valores.append(9)
valores.append(4)

for v in valores:
    #print(f'{v}...')
    print(f'{v}...', end='') #para imprimir na mesma linha

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!') 
print('Cheguei ao final da lista!')

a = [2, 3, 4, 7]
# b = a
b = a[:] # cria uma cópia da lista a
print(f'Lista A: {a}')
print(f'Lista B: {b}')
b[2] = 8 # modifica as duas listas porque o Python cria uma ligação
print(f'Lista A: {a}')
print(f'Lista B: {b}')