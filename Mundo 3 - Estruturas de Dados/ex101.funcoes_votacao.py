# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
def voto(ano):
    from datetime import date #utilizar a importacao dentro da funcao economiza memoria
    idade = date.today().year - ano
    if idade < 16:
        print(f'Voce tem {idade} anos: VOTO NEGADO')
    elif idade > 70 or 16 <= idade < 18:
        print(f'Voce tem {idade} anos: VOTO OPCIONAL')   
    else:
        print(f'Voce tem {idade} anos: VOTO OBRIGATORIO')
    

a = int(input('Digite o ano que voce nasceu: ')) 
voto(a)