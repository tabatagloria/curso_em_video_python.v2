# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'Santo':

cidade = str(input('Digite o nome da cidade: ')).strip()
santo = cidade.lower().split()[0]
print('santo' in santo)