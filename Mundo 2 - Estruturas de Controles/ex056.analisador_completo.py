# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre: A média de idade do grupo; Qual é o nome do homem mais velho e Quantas mulheres têm menos de 20 anos:

media = 0
nome2 = ''
age = 0
mulher = 0
for i in range(4):
    print('Pessoa {}:'.format(i + 1))
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    sexo = int(input('Digite:\n1 - Masculino\n2 - Feminino\n'))
    media += idade
    if sexo == 1:
        if idade > age:
            age = idade
            nome2 = nome
    if sexo == 2 and idade < 20:
        mulher += 1
m = media / 4
print('A média de idade das pessoas são {}, o nome do homem mais velho é {} e a quantidade de mulheres com menos de 20 anos é {}.'.format(m, nome2, mulher))




    
    