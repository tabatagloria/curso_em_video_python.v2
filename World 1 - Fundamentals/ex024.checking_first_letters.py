# Create a program that reads the name of a city and says whether or not it starts with the name 'Saint':

city = str(input('Enter the city name: ')).strip()
saint = city.lower().split()[0]
print('saint' in saint)