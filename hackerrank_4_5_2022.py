# python - Basic Data Types
# List Comprehension

list1 = [1, 2, 3, 4, 5]
# first part - what goes in list - element
# second part - for loop, iterater definition, any iterable
# third part (optional) - if statement
list2 = [x*x for x in list1 if x % 5 == 0]
print(list2)

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
# element = (num, letter)
# nested loops
list3 = [(num, letter) for num in list1 for letter in list2]
print(list3)

# hackerrank problem
x = 1
y = 1
z = 2
n = 3
# answer
possible_coordinates = [[i, j, k] for i in range(
    x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
print(possible_coordinates)

# hackerrank problem 2 - find runner up
arr = [2, 3, 6, 6, 5]
# create list
list1 = list(arr)
# sort list
list1.sort()
i = 2
# walk backwards through list until second highest score is found
while list1[-i] == list1[-1]:
    i += 1
print(list1[-i])  # print runner up / second highest score
