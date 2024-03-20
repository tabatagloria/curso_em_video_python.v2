# Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$0.50 por km para viagens de até 200km e R$0.45 para viagens mais longas:

km = float(input('Digite a distância da viagem em km: '))
if km <= 200:
    total = km * 0.50
else:
    total = km * 0.45
print('O valor da passagem é R${:.2f}'.format(total))