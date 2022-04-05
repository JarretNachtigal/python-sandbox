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

# third hackerrank problem - might not run due to input()

# scores = {}
# lowest_score = 9223372036854775807
# second_lowest_score = 9223372036854775807
# for _ in range(int(input())):
#     name = input()
#     score = float(input())
#     # given names and grades
#     # print names of students with second lowest grade

#     # add each student to dict
#     scores[name] = score
#     # keep track of lowest and second lowest
#     # if score is lower than second lowest, check lowest
#     if second_lowest_score > score or lowest_score == None:
#         # if score is lowest, shift
#         if lowest_score > score:
#             second_lowest_score = lowest_score
#             lowest_score = score
#         # if score is second lowest, replace
#         else:
#             second_lowest_score = score
# list1 = [name for name, score in scores.items() if score == second_lowest_score]
# list1.sort() # for the hackerrank answers - alphabetical
# for name in list1:
#     print(name)
