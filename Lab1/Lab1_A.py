user_Input = float(input("Enter the temperature in Celsius: "))
temp_In_Fahrenheit = round(user_Input * (9 / 5) + 32, 1) # Convert to F
print(f'That is {temp_In_Fahrenheit} degrees Fahrenheit!')
