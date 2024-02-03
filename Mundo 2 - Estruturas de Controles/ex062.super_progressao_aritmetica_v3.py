# Melhore o Desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.
t = int(input('Digite o primeiro termo da progressão aritmética: '))
r = int(input('Digite o primeiro termo da progressÃo aritmética: '))
nt = 0
count = 0
count2 = 0
mais = 10
while mais != 0:
    nt = nt + mais
    while count <= nt:
       count += 1
       pa = t
       t += r
       print(pa, end = ' -> ')
    print('Pausa')
    mais = int(input('Digite quantos termos deseja calcular a mais: '))
print('Fim do programa: ')

   