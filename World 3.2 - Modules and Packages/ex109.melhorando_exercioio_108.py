#Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

from utilidadesCeV import moeda

n = float(input('Digite o preco: $'))
print(f'A metade de {moeda.moeda(n)} eh ${moeda.metade(n, True)}')
print(f'O dobro de {moeda.moeda(n)} eh ${moeda.dobro(n, True)}')
print(f'Aumentando 10%, temos ${moeda.aumentar(n, 10, True)}')
print(f'Diminuindo 20%, temos ${moeda.diminuir(n, 20, True)}')