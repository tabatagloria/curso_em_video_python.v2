from lib.interface import *

def fileExist(name):
    try:
        a = open(name, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
    
def createFile(name):
    try:
        a = open(name, 'wt+')
        a.close()
    except:
        print('Error!')
    else:
        print(f'Arquivo {name} criado com sucesso')
        
        
def readFile(name):
    try:
        a = open(name, 'rt')
    except:
        print('Error!')
    else:
        header('RECORDS')
        for line in a:
            data = line.split(';')
            data[1] = data[1].replace('\n', '')
            print(f'{data[0]:<30}{data[1]:>3} years')
            
    finally:
        a.close()
        
        
def register(fl, name='unknown', age=0):
    try:
        a = open(fl, 'at')
    except:
        print('Error!')
    else:
        try:
            a.write(f'{name};{age}\n')
        except:
            print('Error!')
        else:
            print(f'New register from {name} added.')
            a.close()
    
        
    