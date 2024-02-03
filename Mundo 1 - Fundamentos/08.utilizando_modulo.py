# import => importa todas as funcionalidades de uma biblioteca'
# from/import => importa uma funcionalidade específica de uma biblioteca
# math => a biblioteca math é utilizado para funções matemáticas. Exemplo:
# ceil => arredondamento para cima.
# floor => arredondamento para baixo.
# trunc => função truncade que elimina o número da vírgula pra frente.
# pow => função power utilizado para potência.
# sqrt => utilizada para calcular raiz quadrada.
# factorial => utilizada para cálculos fatoriais.
# Exemplo prático:
print('Utilizando import:')
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é {}'.format(num, raiz))

print('Utilizando from/import:')
from math import sqrt
n = int(input('Digite um número: '))
r = sqrt(n) 
print('A raiz de {} é {}'.format(n, r))

print('Números rondômicos: ')
import random
number = random.random() # números reais
print(number)
number = random.randit(1,10) # números inteiros
print(number)

from time import sleep
print('Processando...')
sleep(3)
print('Terminado')


