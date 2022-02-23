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
            print(current_page, page_turns)

    # number of page turns from front
    else:
        print("from front")
        page_turns = 1
        while current_page + 1 < p and current_page + 2 < p:
            current_page += 2
            page_turns += 1
            print(current_page, page_turns)
    return page_turns


print(pageCount(7, 3))
print(pageCount(5, 4))
print(pageCount(6, 2))
