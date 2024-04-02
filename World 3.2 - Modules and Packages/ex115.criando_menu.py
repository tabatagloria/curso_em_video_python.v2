# "Create a small modularized system that allows registering individuals by their name and age in a simple text file. The system will only have 2 options: register a person and list all registered individuals."

from lib.interface import *
from lib.file import *
from time import sleep

fl = 'cursoemvideo.txt'

if not fileExist(fl):
    createFile(fl)

while True:
    answer = menu(['Registered', 'List', 'End'])
    if answer == 1:
        header('NEW REGISTER')
        name = input('Name: ')
        age = readInt('Age: ')
        register(fl, name, age)
    elif answer == 2:
        readFile(fl)
    elif answer == 3:
        header('Finalizing the program...')
        break
    else:
        print('Erro! Enter a valid option: ')
    sleep(2)



