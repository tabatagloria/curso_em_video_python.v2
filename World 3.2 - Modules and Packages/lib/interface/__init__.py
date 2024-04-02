def readInt(msg):
    while True:
        try:
            number = int(input(msg))
        except(ValueError, TypeError):
            print('Error! Please enter a valid integer number.')
        except(KeyboardInterrupt):
            print('User interrupted data entry.')
        else:
            break
    return number


def line(size = 42):
    return '-' * size


def header(txt):
    print(line())
    print(txt.center(42))
    print(line())
    

def menu(list):
    header('MAIN MENU')
    count = 1
    for item in list:
        print(f'{count} - {item}')
        count += 1
    print(line())
    option = readInt('Enter option: ')
    return option