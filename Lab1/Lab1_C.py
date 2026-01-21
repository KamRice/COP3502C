year1Input = (int(input("Enter the year for date 1: ")))
month1Input = (int(input("Enter the month for date 1: ")))
day1Input = (int(input("Enter the day for date 1: ")))
year2Input = (int(input("Enter the year for date 2: ")))
month2Input = (int(input("Enter the month for date 2: ")))
day2Input = (int(input("Enter the day for date 2: ")))

diffYears = (year1Input - year2Input) * 12 * 30
diffMonths = (month1Input - month2Input) * 30
diffDays = day1Input - day2Input

diffTotal = abs(diffYears + diffMonths + diffDays)

print(f"The difference between {month1Input}/{day1Input}/{year1Input} and {month2Input}/{day2Input}/{year2Input} is {diffTotal} days!")