# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações: - Quantidade de notas; – A maior nota;  – A menor nota; – A média da turma; – A situação (opcional).

def notas(n, sit=True):
    """
        -> Funcao que retorna um dicionario com as informacoes de uma turma de alunos.
        ; param n: lista com as notas da classe
        ; param sit: parametro opcional, mostra a situacao da turma
    """
    m = sum(n)/len(n)
    if m < 5:
        s = 'ruim'
    elif 5 > m < 8: 
        s = 'boa'
    else:
        s = 'otima'
    alunos = {'total': len(n), 'maior': max(n), 'menor': min(n), 'media': sum(n)/len(n), 'situacao': s }
    return (alunos)
n = notas((3.3, 5.5, 10, 9, 8),sit =True)
print(n)
help(notas)

    
    
    
