# Create an algorithm that reads an employee's salary and shows his new salary, with a 15% increase:

salary = float(input('Enter the salary: $'))
increase = salary + (salary * 0.15)
print('The new salary with the 15% increase is ${:.2f}'.format(increase))