# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade: 1 - se ele ainda vai se alistar ao serviço militar; 2 -  Se é a hora de se alistar; 3 - Se já passou o tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

import datetime
nascimento = int(input('Digite o ano do seu nascimento: '))
ano = datetime.date.today()
alistamento = ano.year - nascimento
if alistamento < 18:
    print('Você tem {} anos e ainda vai se alistar ao serviço militar. Falta {} anos para você se alistar'.format(alistamento, 18 - alistamento))
if alistamento == 18:
    print('Você tem {} anos e deve se alistar ao serviço militar'.format(alistamento))
elif alistamento > 18:
    print('Você tem {} anos e já passou do prazo para o se alistar no serviço militar. Passou {} anos do prazo para o seu alistamento'.format(alistamento, alistamento - 18))



