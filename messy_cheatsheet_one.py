# variables / basic data types
# arrays are not standard?
from array import array

boolean_variable = True
boolean_variable = False
integer_variable = 3
float_variable = 3.3
string_variable = "string"
print(type(string_variable))
# control structures
if boolean_variable == True:
    if integer_variable == 5:
        pass
    pass
elif not boolean_variable:
    pass
else:
    pass

# loops
i = 0
while i < 5:
    i += 1
# 1 2 3 4 5 6 7 8 9
for i in range(1, 10):
    pass
    # print(i)
# methods

# classes


class Thing:
    def __init__(self, thing) -> None:
        self.thing = thing  # class variable


# data structures
# ----- THERE ARE 4 COLLECTION DATA TYPES / ARRAYS (list, tuple, set, dictionary)
# list
list = [1, 2, "three", ["four", 5]]  # list can deal with this
print(list)
# dictionary
dictionary = {"thing": 1, "thing2": 2}
print(dictionary)
print(dictionary["thing"])
# can be looped through
for t in dictionary:
    print(t)

# tuple
# ordered - cannot be reordered
# unchanging - cannot add or remove after creation
# allows duplicates
# can be any data type
twople = ("one", "two", "three")
this_tuple = tuple("one",)  # constructor
single_item_tuple = ("thing",)
print(twople[:2])  # start from beginning, noninclusive
print(twople[1])
print(type(twople))
# check for val exist in tuple
if "one" in twople:
    print("yup")
# set
# unordered, unchangeable unindexed, no duplicates, any data type
thisset = {"apple", "banana", "cherry"}
print(thisset)  # this will print in a different order everytime (usually)
print(type(thisset))

# array - needs to be imported my numpy (might have to install with pip install numpy)
# basically a java array/ single data type array


# standard libraries
