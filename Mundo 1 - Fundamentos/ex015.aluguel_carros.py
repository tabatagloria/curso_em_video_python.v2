# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60.00 por dia e R$0.15 por km rodado:

dias = int(input('Quantidade de dias do aluguel do carro: '))
km = float(input('Quantos quilômetros foram percorridos: '))
total = (dias * 60) + (km * 0.15)
print('O total a pagr pelo aluguel do carro é R${:.2f}'.format(total))