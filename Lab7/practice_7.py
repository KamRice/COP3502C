practice1 = {
    "one": {"a": 10, "b": 20, "c": 30},
    "two": {"a": 30, "b": 20, "c": 10},
    "three": {"a": 20, "b": 30, "c": 10},
}

sum_of_grades = 0

for key, value in practice1.items():
    for member in value:
        if member == "a":
            sum_of_grades += practice1[key][member]

print(sum_of_grades)
print()

practice2 = [
    {"a": 2, "b": 3, "c": 1},
    {"b": 2, "c": 3},
    {"a": 1, "b": 2, "c": 3},
    {"a": 3, "b": 2, "c": 1},
    {"c": 1, "a": 4},
]

sum_of_grades2 = 0

for member in practice2:
    sum_of_grades2 += member.get("a", 0)

print(sum_of_grades2)
