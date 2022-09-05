# if in - certain collections like dict and list
# time complexity is dependant on data type
# - list O(n),
# - Dict O(1) - O(n) -> when all values have the same hashed value
list_of_things = [1, 2, "thing", True]
if "thing" in list_of_things:
    print("yes")
else:
    print("no")
