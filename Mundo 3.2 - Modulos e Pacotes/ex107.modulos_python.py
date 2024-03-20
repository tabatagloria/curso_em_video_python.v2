# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

from utilidadesCeV import moeda

n = float(input('Digite o preco: $'))
print(f'A metade de {n} eh ${moeda.metade(n)}')
print(f'O dobro de {n} eh ${moeda.dobro(n)}')
print(f'Aumentando 10%, temos ${moeda.aumentar(n, 10)}')
print(f'Diminuindo 20%, temos ${moeda.diminuir(n, 20)}')

