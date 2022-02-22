from numpy import short


def appendAndDelete(s, t, k):
    # Write your code here
    # find number of differing indexes
    # length_difference = math.abs(len(s) - len(t))
    # s becomes t
    difference = 0
    if s in t:
        difference = 2 * (len(t) - len(s))
    elif t in s:
        difference = 2 * (len(s) - len(t))

    if difference <= k:
        print(difference)
        return "Yes"
    else:
        print(difference)
        return "No"


def append_and_delete_two(s, t, k):
    num_changes_needed = 0
    if s == t and k % 2 == 0:
        return "Yes"
    # get long and short lists
    s_list = list(s)
    t_list = list(t)
    i = 0  # loop index and number of letters that are the same at the beginning of the string
    # loop goes until a difference is found
    while i < len(s_list) and i < len(t_list) and t_list[i] == s_list[i]:
        i += 1
    num_changes_needed = len(s_list) - i  # remove steps
    num_changes_needed += len(t_list) - i  # append steps

    # if k = number of needed moves
    if k >= len(s) + len(t):
        print(num_changes_needed)
        return "Yes"
    # if extra moves needed can be done exactly
    elif k >= num_changes_needed and (k - num_changes_needed) % 2 == 0:
        print(num_changes_needed)
        return "Yes"
    # k moves cannot be done to make s into t
    else:
        print(num_changes_needed)
        return "No"


# print(appendAndDelete("aaaaaaaaaa", "aaaaa", 7))
print(append_and_delete_two("aaaaaaaaaa", "aaaaa", 7))
# print(append_and_delete_two("y", "yu", 2))
# print(append_and_delete_two("aba", "aba", 7))
# print(append_and_delete_two("qwerasdf", "qwerbsdf", 6))
