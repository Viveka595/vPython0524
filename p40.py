#Wap to find profit/loss/equal of a product by taking cost price
#and selling price from user input.

cost=float(input('Enter the cost price of product='))
sell=float(input('Enter selling price of product='))
if sell>cost:
    print('Profit')
elif sell<cost:
    print('Loss')
elif cost==sell:
    print('No profit and No Loss equal')
    
