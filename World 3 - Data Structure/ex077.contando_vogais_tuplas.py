# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

words = ('amor', 'amizade', 'mulher', 'familia', 'trabalho', 'respeito')
vogais = []

for i in words:
    for v in i:
        if v == 'a' or v == 'e' or v == 'i' or v == 'o' or v == 'u':
            vogais.append(v)
    print(f'Na palavra {i}, tem as seguintes vogais {vogais}')
    vogais = []

# ou
words = ('amor', 'amizade', 'mulher', 'familia', 'trabalho', 'respeito')
for p in words:
    print(f'\nNa palavra {p} temos ', end = '')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end = ' ')
        
            

            
