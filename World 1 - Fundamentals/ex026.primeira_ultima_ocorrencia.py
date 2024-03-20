# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra 'A';
# Em que posicão ela aparece a primeira vez;
# Em que posição ela aparece a última vez;

frase = str(input('Digite uma frase: ')).strip()
f = frase.lower()
print('Quantas letras A aparecem: {}'.format(f.count('a')))
print('Posição em que aparece a primeira vez: {}'.format(f.find('a') + 1))
print('Posição em que aparece pela última vez: {}'.format(f.rfind('a') + 1))
