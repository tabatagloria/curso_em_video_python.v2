# Create a program that reads how much money a person has in their wallet and shows how many dollars they can buy. Consider US$1.00 = R$3.27

real = float(input('How much do you have: R$'))
dollar = real / 3.27
print('With the value of R${:.2f} you can buy US${:.2f}'.format(real, dollar))