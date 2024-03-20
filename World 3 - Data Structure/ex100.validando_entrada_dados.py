# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from time import sleep
from random import randint

par = []
def sorteia(lista):
    for i in range(5):
        lista.append(randint(0,10))
        par = lista
    print('-=' * 30)
    print('Sorteando 5 numeros...')
    sleep(1)
    print(par)
    somaPar(par)

def somaPar(soma):
    p = 0
    print('-=' * 30)
    for i in soma:
        if i % 2 == 0:
            p += i
    sleep(1)
    print(f'A soma dos numeros pares eh: {p}')

numeros = []
sorteia(numeros)

      

        
