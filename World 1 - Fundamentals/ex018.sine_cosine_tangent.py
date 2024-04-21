# Write a program that reads any angle and shows on the screen the value of its sine, cosine and tangent of that angle: 

from math import sin, cos, tan, radians

angle = float(input('Enter the value of angle: '))
sine = sin(radians(angle))
cosine = cos(radians(angle))
tangent = tan(radians(angle))
print('For the angle {} we have the sine {:.2f}, cosine {:.2f} and tangent {:.2f}'.format(angle, sine, cosine, tangent))