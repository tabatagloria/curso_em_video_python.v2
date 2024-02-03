# Crie um programa onde o usuário possa digitar sete valores númericos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente:

numeros = []
pares = []
impares = []
for i in range(7):
    n = int(input('Digite um número inteiro: '))
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
numeros.append(pares[:])
numeros.append(impares[:])
print(f'A lista com os números cadastrados é {numeros}')
print(f'Sendo os números pares {sorted(numeros[0]) } e os ímpares {sorted(numeros[1])}')
