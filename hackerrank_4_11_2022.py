# 1 - Python/Basic DataTypes/Finding The Percentage

# feed input through stdin

# n = int(input())
# student_marks = {}
# for _ in range(n):
#     name, *line = input().split()
#     scores = list(map(float, line))
#     student_marks[name] = scores
# query_name = input()
# # student_marks = dict - name => scores[]
# # for a given student name - print average score to 2 decimal places
# # ex: 'beta':[30,50,70] = 150/3 = 50.0
# # return 50.0

# if query_name in student_marks:
#     scores_total = 0
#     for i in student_marks[query_name]:  # loop
#         scores_total += float(i)
#     average = scores_total / float(len(student_marks[query_name]))
#     print("{:.2f}".format(average))
# else:  # query not valid
#     print("none")

# ------------------------------------------------

# 2 - Python/Errors and Exceptions/Exceptions

# feed input through stdin

# num_test_cases = int(input()) # number of inputs / loop constraint
# # loop
# for _ in range(num_test_cases):
#     try:
#         nums = input().split(" ") # get input as list
#         a, b = int(nums[0]), int(nums[1]) # set varibles from input list
#         print(a//b) # attempt integer division
#     except ZeroDivisionError as e: # will occur when b == 0
#         print("Error Code:", e)
#     except ValueError as e: # will occur when int(input(--invalid--))
#         print("Error Code:", e)

# ------------------------------------------------------------

# 3 - Python/Errors and Exceptions/Incorrect Regex

# take input through stdin

# import re # regex library?
# num = int(input()) # first input, int, num inputs
# # loop through input
# for _ in range(num):
#     # if input valid regex, output True
#     try:
#         re.compile(input()) # check regex validity
#         print("True")
#     # else, output false
#     except:
#         print("False")

# NOTES
# - string formatting (using a variable in this case
# average = 3.14159
# print("{:.2f}".format(average))
# => 3.14

# integer division
# a//b => integer/floor division

# Exceptions defined one at a time after try
# can use else or finally afterwards
