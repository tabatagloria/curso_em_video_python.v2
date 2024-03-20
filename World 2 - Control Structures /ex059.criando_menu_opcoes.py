# Crie um programa que leia dois valores e mostre um menu na tela : [1] somar [2] multiplicar [3] maior [4] novos números [5] sair do programa. Seu programa deverá realizar a operação solicitada em cada caso.

soma = 0
mult = 0
maior = menor = 0
menu = 0
while menu != 5:
    n1 = float(input('Digite o primeiro valor: '))
    n2 = float(input('Digite o segundo valor: '))
    menu = int(input('Escolha:\n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos Números\n[5] Sair do Programa.\n'))
    if menu == 1:
        soma = n1 + n2
        print('A soma de {} e {} é {}'.format(n1, n2, soma))
    elif menu == 2:
        mult = n1 * n2
        print('A multiplicação de {} e {} é {}'.format(n1, n2, mult))
    elif menu == 3:
        if n1 < n2:
            menor = n1
            maior = n2
            print('O número {} é maior que o número {}'.format(maior, menor))
        elif n1 > n2:
            menor = n2
            maior = n1
            print('O número {} é maior que o número {}'.format(maior, menor))
        else:
            print('Os números digitados foram {} e são iguais.'.format(n1))
    elif menu == 4:
        n1 = float(input('Digite o primeiro valor: '))
        n2 = float(input('Digite o segundo valor: '))
        menu = int(input('Escolha:\n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos Números\n[5] Sair do Programa.'))
    elif menu < 1 or menu > 5:
        print('Opção inválida, tente novamente!')
        n1 = float(input('Digite o primeiro valor: '))
        n2 = float(input('Digite o segundo valor: '))
        menu = int(input('Escolha:\n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos Números\n[5] Sair do Programa.'))
        print('Fim do programa.')