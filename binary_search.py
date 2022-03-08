def binary_search(arr, num):
    # midpoint - index of the number in arr being checked
    # midpoint_value - value of midpoint
    # left - leftmost number
    # right - rightmost number
    midpoint = len(arr) // 2  # floor division
    midpoint_value = arr[midpoint]
    left = 0
    right = len(arr) - 1
    # greed
    if midpoint_value == num:
        return midpoint
    # continue until number is found or left crosses paths with right
    while left <= right:
        midpoint = (right + left) // 2  # this always works -?-
        midpoint_value = arr[midpoint]
        print(midpoint_value)
        # three possible conditions
        if midpoint_value == num:  # number found, return index
            return midpoint
        elif midpoint_value < num:  # num larger, look right
            left = midpoint + 1     # move bounds to just above midpoint
        else:                       # num smaller, look left
            right = midpoint - 1    # move bounds to just below midpoint
    # return where the number would be inserted
    print("not found, number would in inserted at: ")
    return left


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num = 11
print(binary_search(arr, num))

print("abcd" > "abdc")
