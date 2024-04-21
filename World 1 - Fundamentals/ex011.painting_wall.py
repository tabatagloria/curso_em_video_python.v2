# Write a program that reads the width and height of a wall in meters, calculates its area and the amount of paint needed to paint it, knowing that each liter of paint paints an area of 2m2:

width = float(input('Enter the wall width: '))
height = float(input('Enter the wall height: '))
area = weidth * height
print('Your wall has an area of {:.2}m2 and you will need {:.2f} liters of paint.'.format(area, area / 2))
