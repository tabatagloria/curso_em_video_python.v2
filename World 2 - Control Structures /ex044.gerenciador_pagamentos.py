# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento: À VISTA (dinheiro/cheque): 10% de desconto, À VISTA NO CARTÃO: 5% de desconto; em até 2x no cartão: preço normal; 3 ou mais no cartão 20% de juros:

valor = float(input('Digite o valor do produto: R$'))
pagamento = int(input('Escolha a condição de pagamento:\n 1 - À Vista (dinheiro/cheque)\n 2 - À Vista no Cartão\n 3 - 2x no Cartão\n 4 - 3x ou mais no Cartão\n '))
if pagamento == 1:
    print('Total R${:.2f}'.format(valor - (valor * 0.10)))
elif pagamento == 2:
    print('Total R${:.2f}'.format(valor - (valor * 0.05)))
elif pagamento == 3:
    print('Total R${:.2f}'.format(valor))
elif pagamento == 4:
    print('Total R${:.2f}'.format(valor + ( valor * 0.20)))
else:
    print('Opção Incálida! Tente novamente.')
    
