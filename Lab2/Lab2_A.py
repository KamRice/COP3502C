side1 = float(input("Side length 1:"))
side2 = float(input("Side length 2:"))
side3 = float(input("Side length 3:"))

output = ''

if side1 == side2:
    if side2 == side3:
        output = 'an equilateral triangle!'
    else:
        output = 'an isosceles triangle!'
elif side1 == side3:
    output = 'an isosceles triangle!'
elif side2 == side3:
    output = 'an isosceles triangle!'
else:
    output = 'a scalene triangle!'

print('This is', output)