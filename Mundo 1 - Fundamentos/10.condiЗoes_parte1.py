# Condições:

# Estrutura:
# if carro.esquerada():
    # bloco True
# else carro.direita():
    # bloco False

# Exemplos: 
tempo = int(input('Quantos anos tem o seu carro: '))
if tempo <= 3:
    print('Carro novo')
else:
    print('Carro velho')
print('===FIM===')

# Condição simplificada:
tempo = int(input('Quantos anos tem o seu carro: '))
print('Carro novo' if tempo <= 3 else 'Carro velho')
print('===FIM===')



