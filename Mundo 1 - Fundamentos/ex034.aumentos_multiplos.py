# Escreva um programa que pergunte o salário de um funconário e calcule o valor do seu aumento:
# Para salários superiores a R$1250.00, calcule um aumento de 10%;
# para inferiores ou iguais, o aumento é de 15%.

salario = float(input('Qual é o salário do funcionário: R$'))
if salario > 1250.00:
    aumento = (salario * 0.10) + salario
else:
    aumento = (salario * 0.15) + salario
print('O valor do salário com o aumento é de R${:.2f}'.format(aumento))