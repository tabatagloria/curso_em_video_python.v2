# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada: a - de 1 até 10, de 1 em 1; b - de 10 até 0, de 2 em 2; c - uma contagem personalizada:
def contagem(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(cont, end=' ')
            cont += passo
        print('Fim!')
    else:
        cont = inicio
        while cont >= fim:
            print(cont, end=' ')
            cont -= passo
        print('Fim!')

print('Contagem de 1 a 10: s')
contagem(1, 10, 1)
print('Contagem de 10 a 0 de 2 em 2:')
contagem(10, 0, 2)
print('Contagem personalizada: ')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contagem(i, f, p)    
   


   