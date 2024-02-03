# Crie um programa que leia um nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas;
# O nome com todas as letras minúsculas;
# Quantas letras ao todo (sem considerar os espaços;
# Quantas letras tem o primeiro nome;

nome = str(input('Digite um nome completo: ')).strip()
print('Nome em maiúsculo: {}'.format(nome.upper()))
print('Nome em minúsculo: {}'.format(nome.lower()))
print('Quantidade de letras: {}'.format(len(nome.replace(' ', ''))))
print('Quantidade de letras do primeiro nome: {}'.format(len(nome.split()[0])))