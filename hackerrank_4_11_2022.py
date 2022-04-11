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


# NOTES
# - string formatting (using a variable in this case
# average = 3.14159
# print("{:.2f}".format(average))
# => 3.14
