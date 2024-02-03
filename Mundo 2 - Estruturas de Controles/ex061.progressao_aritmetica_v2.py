# Refaça o Desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
t = int(input('Digite o primeiro termo da progressão aritmética: '))
r = int(input('Digite a razão da progreeão aritmética: '))
count = 0
while count < 10:
    count += 1
    pa = t
    t += r
    print(pa, end = ' -> ')
print('Fim')
    


