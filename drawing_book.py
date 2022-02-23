import math


def pageCount(n, p):
    # Write your code here
    if p == 1:
        return 0
    # check if p (search page) is closer to 1 than n (num pages)
    current_page = 1
    page_turns = 0
    odd_num_offset = -1
    if n % 2 == 0:
        odd_num_offset = 1
    if n - p < p:
        print("from back", odd_num_offset)
        current_page = n
        # number of page turns from back
        while current_page > p and current_page + odd_num_offset > p:
            current_page -= 2
            page_turns += 1
            # print(current_page, page_turns)

    # number of page turns from front
    else:
        print("from front")
        page_turns = 1
        while current_page + 1 < p and current_page + 2 < p:
            current_page += 2
            page_turns += 1
            # print(current_page, page_turns)
    return page_turns


def pageCountTwo(n, p):
    if p == 1:
        return 0
    page_turns = 1
    if n - p < p:  # go from back
        offset = -1  # defualt n is odd, both pages on last page
        if n % 2 == 0:  # if n is even, only left page on last page
            offset = 1
        if not p % 2 == 0:  # if p is odd, will be on right side of page, +1 page turn from back unless back page filled
            offset += 1
        print("back", offset)
        page_turns = math.floor(n - p + offset) / 2
    else:  # go from front
        if p % 2 == 0:
            offset = 1  # if p is even, will be on left side, +1 page turn
        else:
            offset = -1  # if p is odd, will be on right side, -1 page turn
        print("front", offset)
        # round down, odd p rounds down by 2 even rounds up by 2
        page_turns = math.floor((p + offset) / 2)
    return int(page_turns)


# print(1, pageCount(7, 3))
# print(2, pageCount(5, 4))
# print(3, pageCount(6, 2))
# print(3, pageCount(6, 3))
# right side n, right side p - double odd from back
print(3, pageCount(37455, 29835))

# print(1, pageCountTwo(7, 3))
# print(2, pageCountTwo(5, 4))
# print(3, pageCountTwo(6, 2))
# print(3, pageCountTwo(6, 3))
# right side n, right side p - double odd from back
print(3, pageCountTwo(37455, 29835))
