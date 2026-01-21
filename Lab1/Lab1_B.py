itemPrice = float(input("Enter the price of the item: "))
salesTax = float(input("Enter the sales tax percentage: "))

total = round(itemPrice + (itemPrice * salesTax/100), 2) #Add sales tax.

print(f'Your total is ${total:.2f}')