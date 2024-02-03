# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços:

frase = str(input('Digite uma frase: ')).strip().replace(' ', '').lower()
palin = frase[::-1]
print('Você digitou {} a frase de trás pra frente é {}'.format(frase, palin))
if frase == palin:
    print('É um palindromo.')
else:
    print('Não é um palíndromo.')