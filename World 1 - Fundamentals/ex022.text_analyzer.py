# Create a program that reads a person's full name and displays: a - The name in all capital letters; b - The name in all lowercase letters; c - How many letters in total (without considering spaces); d - How many letters are in the first name;

name = str(input('Enter the full name: ')).strip()
print('Name in capital letters: {}'.format(name.upper()))
print('Name in lowercase letters: {}'.format(name.lower()))
print('How many letters in total: {}'.format(len(name.replace(' ', ''))))
print('How many letters inthe first name: {}'.format(len(name.split()[0])))