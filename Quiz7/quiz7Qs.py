"""Q1"""
a = [1, 2, [3, 'John', 4], 'Hi']

print(a[2][-1])  # outputs 4
print(a[-1][-1])  # outputs i
print(a[0:-3])  # outputs [1]
print(a[3:0:-2])  # outputs ['Hi', 2]

"""Q2"""
b = [9, 7, 11, 10, 8, 1]
c = [item - 1 for item in b if item % 2 == 1]
c[1:-1] = 'hi'
print(c)  # outputs [8, 'h', 'i', 0]

"""Q3"""
a = [1] + [2]
a.extend([4, 5])
a.append(3)

print(a[3:]) # outputs [5, 3]
