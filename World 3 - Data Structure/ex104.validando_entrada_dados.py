# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

def leiaInt(n):
    num = input(n)
    while num.isnumeric() != True: 
        print('Erro! Digite um numero inteiro valido.')
        num = input(n)
    return num
    

n = leiaInt('Digite um numero: ' )
print(f'Voce digitou o numero {n}')
    