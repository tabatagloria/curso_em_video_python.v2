# Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.

from utilidadesCeV import moeda

n = float(input('Digite o preco: $'))
print(f'A metade de {moeda.moeda(n)} eh ${moeda.moeda(moeda.metade(n))}')
print(f'O dobro de {moeda.moeda(n)} eh ${moeda.moeda(moeda.dobro(n))}')
print(f'Aumentando 10%, temos ${moeda.moeda(moeda.aumentar(n, 10))}')
print(f'Diminindo 20%, temos ${moeda.moeda(moeda.diminuir(n, 20))}')