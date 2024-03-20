# Faça um programa que leia o nome de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente:
# Exemplo: Ana Maria de Souza
# primeiro nome = Ana
# último nome = Souza

nome = str(input('Digite seu nome completo: ')).strip()
n = nome.split()
print('Primeiro nome: {}'.format(n[0]))
print('Último nome: {}'.format(n[-1]))