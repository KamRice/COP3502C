incomeGross = float(input("Enter your total income this year: "))

taxRate = 0
totalTaxes = 0
bracket1 = 11600
bracket2 = 47150
bracket3 = 100525
bracket4 = 191950
bracket5 = 243725
bracket6 = 609350

if incomeGross > bracket6:
    taxRate = .37
    totalTaxes += float(f"{(incomeGross - bracket6) * taxRate:.2f}")
    incomeGross -= incomeGross - bracket6

if incomeGross > bracket5:
    taxRate = .35
    totalTaxes += float(f"{(incomeGross - bracket5) * taxRate:.2f}")
    incomeGross -= incomeGross - bracket5

if incomeGross > bracket4:
    taxRate = .32
    totalTaxes += float(f"{(incomeGross - bracket4) * taxRate:.2f}")
    incomeGross -= incomeGross - bracket4

if incomeGross > bracket3:
    taxRate = .24
    totalTaxes += float(f"{(incomeGross - bracket3) * taxRate:.2f}")
    incomeGross -= incomeGross - bracket3

if incomeGross > bracket2:
    taxRate = .22
    totalTaxes += float(f"{(incomeGross - bracket2) * taxRate:.2f}")
    incomeGross -= incomeGross - bracket2

if incomeGross > bracket1:
    taxRate = .12
    totalTaxes += float(f"{(incomeGross - bracket1) * taxRate:.2f}")
    incomeGross -= incomeGross - bracket1

taxRate = .1
totalTaxes += float(f"{(incomeGross) * taxRate:.2f}")
incomeGross -= 11600

print(f"You owe ${totalTaxes:.2f} this year.")