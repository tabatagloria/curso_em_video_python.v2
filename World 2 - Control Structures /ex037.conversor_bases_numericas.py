# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário; 2 para octal e 3 para hexadecimal:


numero = int(input('Digite um número inteiro: '))
opcao = int(input('1 - Binário \n2 - Octal \n3 - Hexadecimal \nEscolha uma opção: '))
if opcao == 1:
    print('O número {} em binário é {}'.format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('O número {} em octal é {}'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('O número {} em hexadecimal é {}'.format(numero, hex(numero)[2:]))
else:
    print('Opção Inválida! Tente novamente.')