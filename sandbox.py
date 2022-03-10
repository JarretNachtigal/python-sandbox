arr = [1, 2, 3, 4, 5]

print(arr[:4])  # from beginning to index 4 noninclusive
print(arr[1:])  # from index 1 inclusive to end
print(arr[::4])  # index 0, index 4
print(arr[1:][::3])  # index 1, step by 3
print(arr[1:][::-1])  # index 1 and on, reversed
print(arr[::-1])  # reverse
