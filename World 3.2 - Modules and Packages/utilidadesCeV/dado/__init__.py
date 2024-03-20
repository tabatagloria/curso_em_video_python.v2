from utilidadesCeV import moeda

def leiaDinheiro(m):
    while True:
        m = input('Digite o valor: ').replace(',', '.').strip()
        if m.isalpha():
            print('\033[0;31mErro! digite um valor valido!\033[m')
        else:
            d = float(m)
            moeda.resumo(d)
            break
            
            