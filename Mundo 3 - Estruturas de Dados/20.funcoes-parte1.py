'''def titulo(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)


titulo('   CURSO EM VÍDEO   ')
titulo('   APRENDA PYTHON   ')
titulo('   GUSTAVO GUANABARA   ')'''

'''def soma(a, b):
    s = a + b
    print(s)


soma(4, 5)
soma(a = 8, b = 9)
soma(b = 2, a = 1)'''

#quando não sabemos a quantidade de parâmetros:
'''def contador(* num):
    print(num)


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)'''

def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1



valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)


