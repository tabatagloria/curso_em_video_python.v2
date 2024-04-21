# Write a program that reads a number from 0 to 9999 and displays each of the separate digits on the screen. Example: Enter a number: 1834, unit: 4, ten: 3, hundred: 8, thousand: 1

number = int(input('Enter the integer number: '))
print('unit = {}'.format(number // 1 % 10))
print('ten = {}'.format(number // 10 % 10))
print('hundred = {}'.format(number // 100 % 10))
print('thousand = {}'.format(number // 1000 % 10))