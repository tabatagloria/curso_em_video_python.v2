print('====== Tipos Primitivos ====== ')

print('Inteiros -> int()')

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
sum = n1 + n2
print('A Soma entre {} e {} vale {}'.format(n1, n2, sum))
print(type(sum)) # type informa o tipo primitivo

print('Reais -> float()')

n1 = float(input('Digite um número: '))
print(n1)
print(type(n1))

print('Boleanos -> bool()')

n1 = bool(input('Digite um número: '))
print(n1)
print(type(n1))

print('Strings -> str()')

n1 = str(input('Digite algo: '))
print(n1)
print(type(n1))
print(n1.isnumeric()) # se é um número
print(n1.isalpha()) # se é letra
print(n1.isalnum()) # e é alfanúmerico
print(n1.isupper()) # está somente em letrar maiúsculas
