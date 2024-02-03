# Escreva um programa que leia um valor em metros e o exiba convertido em quilômetros, hectômetros, decametros, decímetros, centímetros, milímetros:

m = float(input('Digite o valor em metros: '))
qm = m / 1000
hm = m / 100
dm = m / 10
deci = m * 10
cm = m * 100
mm = m * 1000
print('o valor digitado foi {:.2f} convertido em: \nQuilômetros: {:.2f} \nHectômetros: {:.2f} \nDecâmetros: {:.2f} \nDecímetros: {:.2f} \nCentimetros: {:.2f} \nMilímetros: {:.2f}'.format(m, qm, hm, dm, deci, cm, mm))
