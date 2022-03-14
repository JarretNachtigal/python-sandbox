def saveThePrisoner(n, m, s):
    # Write your code here
    # n - number of prisoners
    # m - number of sweets
    # s - starting chair number (not an index)
    i = m
    count = s
    while i > 1:
        if count < n:
            count += 1
        else:
            count = 1
        print("i", i, "count", count)
        i -= 1
    return count


def saveThePrisonerTwo(n, m, s):
    # Write your code here
    # n - number of prisoners
    # m - number of sweets
    # s - starting chair number (not an index)
    count = s
    remaining_sweets = m
    while remaining_sweets > n:
        remaining_sweets -= n
    count += remaining_sweets
    if count > n:
        count -= n
    return count


print(7 % 19)
print(19 % 7)  # remainder from 19 / 7 = 2 (+ 5)


print(saveThePrisonerTwo(7, 19, 2))  # => 6
