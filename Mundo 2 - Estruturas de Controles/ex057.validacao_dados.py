# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = input('Digite "M" para masculino ou "F" para feminino: ').strip().upper()
while sexo not in 'MF':
    sexo = input('Você digitou um valor inválido! Digite "M" ou "F" : ').strip().upper()
print('Valor válido!\nFim do programa!')