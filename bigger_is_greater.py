from itertools import permutations
from xmlrpc.client import MAXINT


# too slow with large inputs
def bigger_is_greater(w):
    # check all permutations of same length
    # save the lowest one that is ? than w
    # if none are, return "no answer"
    perms = set([''.join(p) for p in permutations(w)])
    min = max(perms)
    for p in perms:
        if p > w and p < min:
            min = p
    if min == w:
        return "no answer"
    return min


# doesn't work for all options
def bigger_is_greater_two(w):
    # start from the end, loop through all
    # i = len(w) - 1
    # compare character at i with character at i - 1
    # if i > i -1, swap and end
    # if end is reached, return "no answer"
    i = len(w)-1
    w_copy = w
    w = list(w)
    while i > 0:
        if w[i] > w[i]:
            w[i], w[i-1] = w[i-1], w[i]  # swap
            if "".join(w) > w_copy:
                return "".join(w)
        i -= 1
    return "no answer"

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
    max = ""  # init  to maxval
    max_index = i  # init at beginning
    while i > 1:
        # print("left", w[i-1], "right", w[i], w[i-1] < w[i])
        if w[i-1] < w[i]:  # if left < right
            # print("before swap", w)
            w[max_index], w[i-1] = w[i-1], w[max_index]  # swap
            # print("before sort", w)
            # sort
            w[i+1: length] = sorted(w[i+1: length])
            # print("after sort", w)
            # print("about to return")
            return "".join(w)
        # keep track of smallest val for swapping purposes
        if w[i] > max:
            max = w[i]
            max_index = i
            # print("max set to", max)
        i -= 1
    return "no answer"


def readFile(fileName):
    fileObj = open(fileName, "r")  # opens the file in read mode
    words = fileObj.readlines()  # puts the file into an array
    fileObj.close()
    return words


def difference(arr, arr_two, original):
    i = 0
    while i < len(arr):
        if not arr[i] == arr_two[i]:
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
thier_ans = readFile("bigger_ans.txt")
for s in big_fucking_test:
    ans.append(bigger_is_greater_three(s))

difference(ans, thier_ans, big_fucking_test)

# ans = bigger_is_greater_three(
#     "dkhc")
# print(ans)

# print("a" < "b")
# print(ans, len(ans))
# print(len("vvvygfabrsqeitgelpxwodhdfyypoyufxnecmrtkbzbhzfbtvnffcmikqoosfzoozssonomkgmtdqfecrqtps"))
# w = ['d', 'k', 'h', 'c']
# i = 1
# length = len(w)
# print(w)
# w[i: length] = sorted(w[i: length])
# print(w)
