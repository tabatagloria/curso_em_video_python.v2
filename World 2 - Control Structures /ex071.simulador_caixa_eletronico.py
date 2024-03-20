# Crie um programa que simule o funcionamento de um caixa eletrônico. No ínício, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS: Considere que o caixa possui cédulas de R$50, R$ 20, R$10 e R$1:

n50 = n20 = n10 = n1 = 0
print('====== Caixa Eletrônico ======')
valor = int(input('Qual valor que deseja sacar (valor inteiro): R$'))
v = valor
while True:
    
    if valor >= 50:
        valor = valor - 50
        n50 += 1
    else:
        if valor >= 20:
            valor = valor - 20
            n20 += 1
        elif valor >= 10:
            valor = valor - 10
            n10 += 1
        elif valor >= 1:
            valor = valor - 1
            n1 += 1
        if valor == 0:
            break
print(f'Foi solicitado o valor R${v:.2f} e foram entregues:\n{n50} cédulas de R$50.00\n{n20} cédulas de R$20.00\n{n10} cédulas de R$10.00\n{n1} cédulas de R$1.00')
    



