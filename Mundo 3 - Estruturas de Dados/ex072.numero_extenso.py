# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extensão, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

continuar = 'S'
numbers = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
while continuar == 'S':
    while True:
        n = int(input('Digite um número inteiro de 0 a 20: '))
        if n > 20 or n < 0:
            print('Você digitou um número diferente do intervalo de 0 e 20.')
        else:
            print(f'Você digitou o número {numbers[n]}')
            break
    continuar = input('Deseja continuar? S/N ').upper().strip()[0]
print('Fim do programa!')
