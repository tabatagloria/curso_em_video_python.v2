# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ele não pode exceder 30% do salário ou então o empréstimo será negado.

valor = float(input('Valor da casa: R$')) 
salario = float(input('Valor do salário do comprador: R$'))
tempo = int(input('Tempo financiamento (anos): '))
prestacao = valor / (tempo * 12)
analise = prestacao / salario * 100
if analise <= 30:
    print('Empréstimo aprovado. O valor da prestação será de R${:.2f}.'.format(prestacao))
else:
    print('Empréstimo Negado. O valor da prestação de R${:.2f}, ultrapassa 30% do salário do comprador.'.format(prestacao))
