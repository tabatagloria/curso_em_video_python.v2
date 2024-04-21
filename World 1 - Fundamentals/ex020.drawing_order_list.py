# The same teacher from the previous challenge wants to draw the order in which the students' homework will be presented. Make a program that reads the names of the four students and shows the order drawn:

from random import sample

student1 = input('Enter the name of the first student: ')
student2 = input('Enter the name of the second student: ')
student3 = input('Enter the name of the third student: ')
student4 = input('Enter the name of the fourth student: ')
list = [student1, student2, student3, student4]
order = sample(list, k=4)
print('The order of presentation is: {}'.format(order))
