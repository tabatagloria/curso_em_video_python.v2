# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
products = ('Caneta', 1.99, 'Borracha', 0.99, 'Caderno', 20.99, 'Folha de Sulfite', 5.99, 'Lápis', 0.50)
for i in range(0, len(products)):
    if i % 2 == 0:
        print(f'{products[i]:.<30}', end = '')
    else:
        print(f'R${products[i]:>7.2f}')
print('-'*40)
        




