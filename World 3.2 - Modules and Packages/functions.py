def readInt(number):
    while True:
        try:
            number = int(input('Enter a integer number: '))
        except(ValueError, TypeError):
            print('Error! Please enter a valid integer number.')
        except(KeyboardInterrupt):
            print('User interrupted data entry.')
        else:
            break
    return number
    
    


def readFloat(number2):
    while True:
        try:
            number2 = float(input('Enter a real number: '))
        except(ValueError, TypeError):
            print('Error! Please enter a valid real number.')
        except(KeyboardInterrupt):
            print('User interrupted data entry.')
            break
        else:
            break
    return number2


    