# Create an algorithm that reads the price of a product and shows its new price, with a 5% discount:

price = float(input('Price of product: $'))
discount = price - (price * 0.05)
print('The final price with the 5% discount is ${:.2f}'.format(discount))