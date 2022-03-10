def picking_numbers(a):
    a = sorted(a)
    count = 1
    longest_count = 0
    i = 0
    length = len(a)
    current_num = a[i]
    while i < length-1:
        if abs(current_num - a[i+1]) == 1 or abs(current_num - a[i+1]) == 0:
            count += 1
        else:
            count = 1
            current_num = a[i+1]
        if count > longest_count:
            longest_count = count
        i += 1
    return longest_count


arr = []
for i in range(0, 100):
    arr.append(66)

print(picking_numbers(arr))
