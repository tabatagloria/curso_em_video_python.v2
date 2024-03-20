# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep

def maior(lista):
    print('-=' * 50)
    print('Analisando os valores informados...')
    sleep(1)
    print(f'{lista}, foram informados {len(lista)} valores.')
    sleep(1)
    print(f'O maior valor sendo {max(lista)}.')
valores = [1,2,3,4,8,70]
maior(valores)
valores = [0, 5, 8]
maior(valores)
valores = [90, -3, 5, 40]
maior(valores)
valores = [1,2,3,4,5,6,7,8  ]
maior(valores)
