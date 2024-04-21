# Write a program that reads the length of the opposite cathetus and adjacent cathetus of a right triangle, calculates and displays the length of the hypotenuse:

from math import hypot
opposite = float(input('Enter the value of opposite cathetus: '))
adjacent = float(input('Enter the value of adjacent cathetus: '))
hypotenuse = hypot(opposite, adjacent)
print('The hypotenuse oppsite cathetus {} and adjacent {} is {}'.format(opposite, adjacent, hypotenuse))