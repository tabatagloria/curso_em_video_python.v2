print('Operações com strings: ')

print('Fatiamento - pega pedaços da string:') 

frase = 'Curso em vídeo Python'
print(frase[9])
print(frase[9:13])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])

print('Análise da string: ')
print('Método len():')
print(len(frase))

print('Método count():')
print(frase.count('o'))
print(frase.count('o', 0, 13))

print('Método find():')
print(frase.find('deo'))
print(frase.find('Android'))

print('Operado in:') 
print('Curso' in frase)

print('Transformações de strings: ')
print('Método replace():') #substituição de strings
print(frase.replace('Python', 'Android'))

print('Método upper():')
print(frase.upper())

print('Método lower():')
print(frase.lower())

print('Método capitalize():')
print(frase.capitalize())

print('Método title()')
print(frase.title())

print('Métode sprip()')
frase = '   Aprenda Python  ' #elimina os espaços antes e depois da string
print(frase.strip())
print(frase.rstrip()) #elimina os espaços à direita
print(frase.lstrip()) # elimina os espaços à esquerda

print('Divisão de string:')
print('Método split():') #reindexa a string
print(frase.split())

print('Junção de string: ')
print('Métode join():')
print('-'.join(frase))