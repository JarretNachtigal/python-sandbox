import math


def saveThePrisoner(n, m, s):
    # Write your code here
    # n - number of prisoners
    # m - number of sweets
    # s - starting chair number (not an index)
    i = m
    count = s
    while m > n:
        m -= n
    while i > 1:
        if count < n:
            count += 1
        else:
            count = 1
        print("i", i, "count", count)
        i -= 1
    return count


def saveThePrisonerTwo(n, m, s):
    # n - number of prisoners
    # m - number of sweets
    # s - starting chair number (not an index)
    # return the seat number when m - 1 sweets have been given
    remainder = m % n
    # end on last chair
    if (remainder + s - 1) % n == 0:
        return n
    else:
        return (remainder + s - 1) % n


    # print(7 % 19)
    # print(19 % 7)  # remainder from 19 / 7 = 2 (+ 5)
print(saveThePrisonerTwo(7, 19, 2))  # => 6
print(saveThePrisonerTwo(5, 2, 1))  # => 2
print(saveThePrisonerTwo(5, 2, 2))  # => 3
print(saveThePrisonerTwo(352926151, 380324688, 94730870))  # => 122129406
