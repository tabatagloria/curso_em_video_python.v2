# Create an algorithm that read a number and prints its double, triple and square root:

number = int(input('Enter a number: '))
double = number * 2
triple = number * 3
square_root = number ** (1/2)
print('The number entered is {} its double is {}, its triple is {} and its square root is {:.2f}'.format(number, double, triple, square_root))