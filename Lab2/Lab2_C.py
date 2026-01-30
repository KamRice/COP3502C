convertingFrom = input("Enter the unit you are converting from: ").upper()
convertingTo = input("Enter the unit you are converting to: ").upper()
temperatureOriginal = float(
    input(f"Enter the temperature in {convertingFrom[0].upper() + convertingFrom[1:].lower()}: "))
output = 0.0

if convertingFrom == "KELVIN":
    if convertingTo == "FAHRENHEIT":
        output = temperatureOriginal * (9 / 5) - 459.67
    elif convertingTo == "CELSIUS":
        output = temperatureOriginal - 273.15
    else:
        output = temperatureOriginal
elif convertingFrom == "CELSIUS":
    if convertingTo == "FAHRENHEIT":
        output = (temperatureOriginal * (9 / 5)) + 32
    elif convertingTo == "KELVIN":
        output = temperatureOriginal + 273.15
    else:
        output = temperatureOriginal
else:
    if convertingTo == "CELSIUS":
        output = (temperatureOriginal - 32) / (9 / 5)
    elif convertingTo == "KELVIN":
        output = (temperatureOriginal + 459.67) * 5 / 9
    else:
        output = temperatureOriginal

print(f"That is {output:.1f} degrees {convertingTo[0].upper() + convertingTo[1:].lower()}.")
