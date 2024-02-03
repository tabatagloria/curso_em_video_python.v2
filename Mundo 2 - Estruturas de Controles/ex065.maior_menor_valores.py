# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
continuar = ' '
n = 0
media = 0
soma = 0 
maior = 0
menor = 0
cont = 0 
while continuar != 'N':
    n = int(input('Digite um número: '))
    continuar = input('Deseja continuar? S/N ').upper().strip()[0]
    soma += n
    cont += 1
    media = soma / 2
    if cont == 1:
        maior = menor = n
    else:
         if n >= maior:
             maior = n
         elif n <= menor:
             menor = n
   
print('A média dos valores digitados foi {}. O maior valor digitado foi {} e o menor valor digitado foi {}'.format(media, maior, menor))
print('Fim do programa!')
