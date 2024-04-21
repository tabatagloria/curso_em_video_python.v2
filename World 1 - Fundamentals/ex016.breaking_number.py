# Create a program that reads any real number from the keyboard and displays its entire portion on the screen. Example: Enter a number: 6,127, the number 6,217 has an integer part of 6.

from math import trunc
number = float(input('Enter the real number: '))
part = trunc(number)
print('The entire portion of {} is {}'.format(number, part))