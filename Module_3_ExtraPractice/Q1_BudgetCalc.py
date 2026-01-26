allowedBudget = float(input("What is your budget? "))
basicTickets = int(input("How many basic tickets would you like to purchase? "))
lowerLevelTickets = int(input("How many lower level tickets would you like to purchase? "))
hotDogs = int(input("How many hot dogs would you like to purchase? "))
fountainDrinks = int(input("How many fountain drinks would you like to purchase? "))
jerseys = int(input("How many jerseys would you like to purchase? "))

basicTicketPrice = 25.63
lowerLevelTicketPrice = 75.34
hotDogsPrice = 9.10
fountainDrinksPrice = 6.99
jerseyPrice = 115.78

expenditure = round(
    basicTickets * basicTicketPrice + lowerLevelTickets * lowerLevelTicketPrice + hotDogs * hotDogsPrice + fountainDrinks * fountainDrinksPrice + jerseys * jerseyPrice,
    2)

print(
    "\nThe cost of each item is shown below:\nBasic Ticket: $25.63\nLower Level Ticket: $75.34\nHot Dog: $9.10\nFountain Drink: $6.99\nJersey: $115.78\n")

if allowedBudget > expenditure:
    print(f"You are within the budget! You have ${round(allowedBudget - expenditure, 2)} leftover to spend.\n")
else:
    print(f"You are over the budget! You have spent ${round(expenditure - allowedBudget, 2)} over the budget.\n")
