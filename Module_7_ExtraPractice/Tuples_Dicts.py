# List Declaration
### Lists are Mutable, I.E. they can be changed.
List_a = [1, 3, 4, 2]

# Tuple Declaration
### Tuples are Immutable, and unlike list do not support Item Reassignment.
Tuple_a = (1, 3, 4, 1)
# Tuples can be declared without the Parenthesis, but in general we declare them using Parenthesis.
Tuple_Alt = 1, 3, 4, 1
Tuple_Empty = ()

print(f"Tuple_a: {type(Tuple_a)} --- Tuple_Alt: {type(Tuple_Alt)}")
# OUTPUTS: Tuple_a: <class 'tuple'> --- Tuple_Alt: <class 'tuple'>

print()

###Tuples can be combined as well.
Tuple_1 = (1, 2, 3)
Tuple_2 = ("a", "b", "c")
Tuple_1_2 = Tuple_1 + Tuple_2
print(Tuple_1_2)

print()

###Tuples can be converted to a List object with the list() Command.
Conv_Tuple_List = list(Tuple_1_2)
print(type(Conv_Tuple_List))

print()

###Tuples are iterable, (Not inclusive of the upper bound)
print(Tuple_1_2[0:2])

print()

###Tuple unpacking where you assign individual variables to take the values of
### an existing Tuple Object
Tuple_To_Unpack = (1, 2, 3, 4)
a, b, c, d = Tuple_To_Unpack

print(a, b, c, d)

### if you only want it semi unpacked you use a * modifier.
a, *b = Tuple_To_Unpack
print(a, b)

*a, b = Tuple_To_Unpack
print(a, b)

a, *b, c = Tuple_To_Unpack
print(a, b, c)

### can not have multiple Starred variables in Tuple Unpacking Assignment, will error.

### Standard Python Commands work on Tuples.

Tuple_Random = (1, 4, 2, 1, 66, 3, 0, 2, 2, 2)

print()
print(f"len: {len(Tuple_Random)}")
print(f"max: {max(Tuple_Random)}")
print(f"count of 2: {Tuple_Random.count(2)}")
print(f"index of 4: {Tuple_Random.index(4)}")
# Index will return first occurrence of requested member.
print(f"index of 2: {Tuple_Random.index(2)}")

print()

### The built in Enumerate() function iterates over a sequence and provides
### an interation counter:

Tuple_To_Crawl = (1, 4, 2, 6, 33, 1, 12)

for index, item in enumerate(Tuple_To_Crawl):
    print(f"Index: {index} : {item}")

print()

"""
|*|*|*|*|*|
Dictionaries
|*|*|*|*|*|
"""

###Dictionaries are considered "Containers" that means that they are NOT ORDERED.
### A dictionary provides a "Container" of values that are accessed by a key,
### resulting in a Key:value pair dynamic.

my_dict = {"Key": "Value", "Age": 35, "Name": "Max"}

print(f"my_dict: {my_dict}")

print(f"my_dict[\"Key\"]: {my_dict["Key"]}")

### Dicts are Mutable and can be changed or added to.

my_dict["Key"] = "New Value"
print(f"my_dict[\"Key\"]: {my_dict["Key"]}")

my_dict["New Key"] = "Added Value"
print(f"my_dict[\"Key\"]: {my_dict["New Key"]}")

###You can remove Key/Value Pairs as well.

print(f"my_dict: {my_dict}")
del my_dict["New Key"]
print(f"my_dict: {my_dict}")

print()

### You can iterate over a Dict as follows:
for key, value in my_dict.items():
    print(f"Key: {key} --- Value: {value}")

print()

###Dictionarie methods

# dict.get(targetKey, defaultReturn)
print(my_dict.get("Age", "No age found"))
print(my_dict.get("Address", "No Address found"))
my_dict["Address"] = "1234 Fake St."
print(my_dict.get("Address", "No Address found"))

print()

# dict1.update(dict2)
# Merges two dictionaries together, where existing entries in dict1 are
# overwritten by the value is dict2 IF they exist in dict2.

dict1 = {"name": "DudeMan", "age": 69, "Occupation": "Supercross Champ"}
dict2 = {"Occupation": "Mechanic", "Address": "8114 Bush Clover"}

print(dict1)
print(dict2)

print()

print(f"dict1.update(dict2): \n\n{dict1.update(dict2)}")

print()

"""
|*|*|*|*|*|
Sets
|*|*|*|*|*|
"""

###Sets are unordered collection of UNIQUE elements.

###Sets are defined using curly braces (like Dictionaries)

my_set = {1, 2, 3, 4, 4, 4, 4, 4, 5, 6}

### Notice that the 4 in this set only "Shows" one time in the output
print(f"only one 4: {my_set}")

print()

###To declare an empty Set:

a = set()

print(f"{a} - {type(a)}")

print()

###Sets can be combined using the union method set_1.union(set_2)

set_1 = {1, 2, 3}
set_2 = {4, 5, 6}
combined_set = set_1.union(set_2)

print(set_1, set_2, combined_set)

print()

### also make note of the set_a.intersection(set_b) Method that returns any
### elements from both sets that are present in both sets

set_a = {2, 3, 4}
set_b = {3, 4, 5}
set_intersection = set_a.intersection(set_b)

print(set_a, set_b, set_intersection)

print()

### there is also the set_a.difference(set_b) method, that removes all the
### elements from set_a that are present in set_b and returns that set.

set_diff = set_a.difference(set_b)

print(set_a, set_b, set_diff)

print()

### Sets are Mutable and can be changed

set_new = set()  # Empty Set Declaration

print(set_new)

set_new.add(1)

print(f"add 1 to set via set_new.add(1): {set_new}")
set_new.update({2, 3, 4})
print(f"add multiple elements to set via set_new.update({"{"}2, 3, 4{"}"}): {set_new}")

print()
print()
print()


print()

my_dict = {'lion':{'color':'yellow-brown','legs':4},
           'elephant':{'color':'gray','legs':4},
           'giraffe':{'color':'spotted','legs':4}}

total_legs = sum(animal['legs'] for animal in my_dict.values())

print(total_legs)

print()

