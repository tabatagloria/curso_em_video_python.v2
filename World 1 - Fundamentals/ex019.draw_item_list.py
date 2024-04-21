# A teacher wants to draw one of his four students to erase the board. Make a program that helps him, reading their name and writing the name of the chosen one.

from random import choice


student1 = input('Enter the name of the first student: ')
student2 = input('Enter the name of the second student: ')
student3 = input('Enter the name of the third student: ')
student4 = input('Enter the name of the fourth student: ')
list = [student1, student2, student3, student4]
draw = choice(list)
print('The chosen student is: {}'.format(draw))