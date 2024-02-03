from statistics import multimode


print('====== Operadores Aritiméticos =======')

print('Adição (+):')
soma = 5 + 2
print ('5 + 2 = {}'.format(soma))

print('Subtração (-):')
sub = 5 - 2
print ('5 - 2 = {}'.format(sub))

print('Multiplicação (*):')
mult = 5 * 2
print ('5 * 2 = {}'.format(mult))

print('Divisão (/):')
div = 5 / 2
print ('5 / 2 = {}'.format(div))

print('Exponenciação (**): ')
exp = 5 ** 2
print ('5 ** 2 = {}'.format(exp))

print('Raiz Quadrada: ')
r = 5 ** (1/2)
r2 = pow(5,2)
print('5 ** (1/2) = {:.2f}'.format(r))
print ('pow(5,2) = {:.2f}'.format(r2))

print('Divisão Inteira (//)')
div_int = 5 // 2
print ('5 // 2 = {}'.format(div_int))

print('Resto da Divisão (%):')
resto = 5 % 2
print ('5 % 2 = {}'.format(resto))

print('Ordem de precedência:')
print('Primeiro ()')
print('Segundo **')
print('Terceiro * / // %')
print('Quarto + -')