from decimal import DivisionUndefined
from collections import OrderedDict

# def divisible_sum_pairs(arr, k):
#     # return number of pairs that are divisible by k when added together
#     # AND first is less than second
#     i = 0
#     count = 0
#     while i <= len(arr) - 1:
#         j = i
#         while j < len(arr) - 1:
#             # if first is larger, pass
#             if arr[i] > arr[j]:
#                 pass
#             j += 1
#             if (arr[i] + arr[j]) % k == 0:
#                 count += 1
#         i += 1
#     return count


# print(divisible_sum_pairs([1, 2, 3, 4, 5, 6], 5))


# takes in an array of ints/ bird id numbers
# count and return highest number
# if tied, return lower id

def readFile(fileName):
    fileObj = open(fileName, "r")  # opens the file in read mode
    words = fileObj.read().split()  # puts the file into an array
    fileObj.close()
    return words


def migratory_birds(arr):
    birds = {}  # hold bird id and numbers
    for bird_id in arr:
        if bird_id in birds:  # if bird_id exists in dict
            birds[bird_id] += 1
        else:
            birds[bird_id] = 1
    # return highest #
    # dictonaries are ordered in 3.7+ so this gets the lowest by default
    birds_items = birds.items()
    sorted_birds = OrderedDict(sorted(birds_items))
    max_key = max(sorted_birds, key=birds.get)
    # print(birds[max_key])
    return max_key


arr = readFile("birds.txt")
# print(migratory_birds([1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]))
print(migratory_birds(arr))
