# Create a Python script that reads a value in meters and prints it converted to kilometers, hectometers, decameters, decimeters, centimeters, and millimeters:

meters = float(input('Enter the value in meters: '))
kilometers = meters / 1000
hectometers = meters / 100
decameters = meters / 10
decimeters = meters * 10
centimeters = meters * 100
millimeters = meters * 1000
print('The value entered was {:.2f} meters, converted to: \nKilometers: {:.2f} \nHectometers: {:.2f} \nDecameters: {:.2f} \nDecimeters: {:.2f} \nCentimeters: {:.2f} \nMillimeters: {:.2f}'.format(meters, kilometers, hectometers, decameters, decimeters, centimeters, millimeters))
