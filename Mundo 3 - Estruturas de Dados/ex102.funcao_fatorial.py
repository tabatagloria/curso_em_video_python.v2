# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um numero.
    ;param n: O numero a ser calculado.
    ;param show: (opcional) Mostrar ou nao a conta.
    ;return: retorna o valor do fatorial de um numero n.
    """
    f = 1   
    for i in range(num, 0, -1):
        if show == True:
            print(i, end=' ')
            if i > 1:
                print(f' x ', end = '')
            else:
                print(' = ', end='')
        f *= i
    return(f)

fatorial(5, True)