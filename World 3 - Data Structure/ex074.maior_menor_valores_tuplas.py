# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import sample
numbers = tuple(sample(range(1, 10),5))
print(f'Os números gerados foram: {numbers}')
print(f'Sendo o menor valor {min(numbers)} e o maior {max(numbers)} ')