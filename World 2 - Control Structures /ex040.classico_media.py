# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final com a média atingida: Média abaixo de 5.0: REPROVADO; Média entre 5.0 e 6.9: RECUPERAÇÃO; Média 7.0 ou superior: APROVADO:

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
if media < 5:
    print('REPROVADO. Média atingida {:.1f}'.format(media))
elif media >= 5 and media <= 6.9:
    print('RECUPERAÇÃO. Média atingida {:.1f}'.format(media))
else:
    print('APROVADO. Média atingida {:.1f}'.format(media))