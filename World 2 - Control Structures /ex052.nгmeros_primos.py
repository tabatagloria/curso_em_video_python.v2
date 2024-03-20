# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo:

n = int(input('Digite um número inteiro: '))
count = 0
for x in range(1, n + 1):
   if n % x == 0:
      count += 1
if count == 2:
   print('O número digitado é primo.')
else:
   print('O número digitado não é primo.')
    