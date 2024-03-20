# Faça um programa que leia um número qualquer e mostre o seu fatorial. Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120


n =  int(input('Digite um número: '))
count = n
fatorial = 1
print('O cálculo de {}! = '.format(n), end = '')
while count > 0 :
    print('{}'.format(count), end = '')
    print(' x ' if count > 1 else ' = ', end = '')
    fatorial *= count
    count -= 1
print('{}'.format(fatorial))

    

