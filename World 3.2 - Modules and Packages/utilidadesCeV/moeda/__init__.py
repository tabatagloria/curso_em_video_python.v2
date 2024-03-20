def aumentar(n, t, format=False):
    resp = n + (n * t/100)
    return resp if format == False else moeda(resp)


def diminuir(n, t, format=False):
    resp = n - (n * t/100)
    return resp if format == False else moeda(resp)


def dobro(n, format=False):
    resp = n * 2
    return resp if format == False else moeda(resp)

def metade(n, format=False):
    resp = n / 2
    return resp if format == False else moeda(resp)


def moeda(n):
    resp = format(n, '.2f').replace('.', ',')
    return resp

def resumo(n, t=10, p=20):
    print('-' * 30)
    print('RESUMO DE VALOR'.center(30))
    print('-' * 30)
    print(f'Valor analisado: \t${moeda(n)}')
    print(f'Metade do valor: \t${metade(n, True)}')
    print(f'Dobro do valor: \t${dobro(n, True)}')
    print(f'{t}% de aumento: \t${aumentar(n, t, True)}')
    print(f'{p}% de reducao: \t${diminuir(n, p, True)}')
    print('-' * 30)