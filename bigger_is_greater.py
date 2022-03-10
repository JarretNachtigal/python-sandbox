from itertools import permutations


# too slow with large inputs
# def bigger_is_greater(w):
# # check all permutations of same length
# # save the lowest one that is ? than w
# # if none are, return "no answer"
# perms = set([''.join(p) for p in permutations(w)])
# min = min(perms)
# for p in perms:
#     if p > w and p < min:
#         min = p
# if min == w:
#     return "no answer"
# return min


# doesn't work for all options
# def bigger_is_greater_two(w):
#     # start from the end, loop through all
#     # i = len(w) - 1
#     # compare character at i with character at i - 1
#     # if i > i -1, swap and end
#     # if end is reached, return "no answer"
#     i = len(w)-1
#     w_copy = w
#     w = list(w)
#     while i > 0:
#         if w[i] > w[i]:
#             w[i], w[i-1] = w[i-1], w[i]  # swap
#             if "".join(w) > w_copy:
#                 return "".join(w)
#         i -= 1
#     return "no answer"

# got ans in theory, didnt read code
# DOESN'T WORK


def bigger_is_greater_three(w):
    # start from the end, loop through all
    # i = len(w) - 1
    # compare character at i with character at i - 1
    # if i > i -1, swap and end
    # if end is reached, return "no answer"
    i = len(w)-1
    w = list(w)
    length = len(w)-1
    # print(length)
    min = ""  # init  to minval
    min_index = i  # init at beginning
    while i > 0:
        # keep track of smallest val for swapping purposes
        if w[i] < min:
            min = w[i]
            min_index = i
        # print("left", w[i-1], "right", w[i], w[i-1] < w[i])
        if w[i-1] < w[i]:  # if left < right
            # print("before swap", w)
            w[min_index], w[i-1] = w[i-1], w[min_index]  # swap
            # print("before sort", w)
            # sort
            temp = w[i+1:][::-1]
            # temp = sorted(w[i: length+1])
            w[i:length+1] = temp
            # print("after sort", w)
            # print("about to return")
            return "".join(w)
            # print("min set to", min)
        i -= 1
    return "no answer"


def bigger_is_greater_four(w):
    result = ""
    n = len(w)
    w = list(w)

    i = n-2

    while i >= 0 and w[i] >= w[i+1]:
        i -= 1

    if i == -1:  # no answer
        result = "no answer"
    else:
        j = n-1  # last letter of string
        while j >= i and w[j] <= w[i]:  # while j > index of small left char
            j -= 1

        w[i], w[j] = w[j], w[i]
        # sort numbers after i (to the right of the small left char index)
        w = "".join(w)
        result = w[:i+1] + w[i+1:][::-1]  # [w from i+1 inclusive], [reversed]
    return result
    # dkhc
    # else, i=d j=c(last char)
    # after swap: hkdc
    # after reverse : hcdk


def readFile(fileName):
    fileObj = open(fileName, "r")  # opens the file in read mode
    words = fileObj.readlines()  # puts the file into an array
    fileObj.close()
    return words


def difference(arr, arr_two, original):
    i = 0
    while i < len(arr):
        str_one = str(arr[i])
        str_two = str(arr_two[i])
        if str_one != str_two:
            print("original", original[i])
            print("my answer:", arr[i], "at index", i)
            print("their answer:", arr_two[i], "at index", i)
        i += 1


# a = ["a", "i", "s", "k", "e", "b"]
# length = len(a)
# a[3:] = sorted(a[3:]) # first index inclusive, second index noninclusive
# print(a)

big_fucking_test = readFile("bigger.txt")
ans = []
their_ans = readFile("bigger_ans.txt")
for s in big_fucking_test:
    ans.append(bigger_is_greater_four(s))

difference(ans, their_ans, big_fucking_test)
# ans = bigger_is_greater_four("dkhc")
# print(ans)
# their_ans =

# print("a" < "b")
# print(ans, len(ans))
# print(len("vvvygfabrsqeitgelpxwodhdfyypoyufxnecmrtkbzbhzfbtvnffcmikqoosfzoozssonomkgmtdqfecrqtps"))
# w = ['d', 'k', 'h', 'c']
# i = 1
# length = len(w)
# print(w)
# temp = sorted(w[i: length])
# w[i: length] = temp
# print(w)
