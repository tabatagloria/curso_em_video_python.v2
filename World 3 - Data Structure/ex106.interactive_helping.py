# Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.

def ajuda(n):
    help(n)


n = ''
while True:
    n = input('Funcao ou Biblioteca: ').lower()
    if n == 'fim':
        break
    else:
        ajuda(n)