# Write a program that asks for the number of km traveled by a rented car and the number of days for which it was rented. Calculate the price to pay, knowing that the car costs $60.00 per day and $0.15 per km driven:

days = int(input('How many days was the car rented: '))
km = float(input('How many kilometers were traveled: '))
total = (days * 60) + (km * 0.15)
print('The total payable for car rental is ${:.2f}'.format(total))