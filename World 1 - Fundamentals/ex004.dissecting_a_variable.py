# Create a python script that reads something from the keyboard and print on the screen its primitive type and all possible information about it:

msg = input('Enter something: ')
print('Primitive type: {} \nSpace: {} \nNumber: {}\nAlphabetic: {} \nAlphanumeric: {} \nUppercase: {} \nLowercase: {} \nTitle: {}'.format(type(msg), msg.isspace(), msg.isnumeric(), msg.isalpha(), msg.isalnum(), msg.isupper(), msg.islower(), msg.istitle()))