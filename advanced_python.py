# if in - certain collections like dict and list
# time complexity is dependant on data type
# - list O(n),
# - Dict O(1) - O(n) -> when all values have the same hashed value
list_of_things = [1, 2, "thing", True]
if "thing" in list_of_things:
    print("yes")
else:
    print("no")

long_empty_list = [0] * 10
# long_empty_list = [] * 10  # this wont work with empty list
print(long_empty_list)

# copy and square a list
mylist = [1, 2, 3, 4, 5]
b = [i*i for i in mylist]
