# Create a program that reads a person's name and tells if they have 'Silva' in their name:

name = str(input('Enter your name: ')).strip()
print('It has Silva in the name: {}'.format('silva' in name.lower()))