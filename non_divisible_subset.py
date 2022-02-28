# hackerrank
import itertools

# BROKEN


def non_divisible_subset(k, s):
    max_subset = []  # hold combinations from working max subset
    max_subset_sum = s[0]  # hold sum from working max subset
    for i in range(1, len(s)):
        new_arr = itertools.combinations(s, i)
        for array in new_arr:
            # get sum
            subarrays = itertools.combinations(array, 2)
            for arr in subarrays:
                sum = 0
                for j in arr:
                    sum += j
                if sum % k == 0:  # 2 elements in the subarray are divisible by k, end
                    continue
                max_subset_sum = sum
                max_subset = array
    print(max_subset)
    print(max_subset_sum)
    return len(max_subset)


# arr = [19, 10, 12, 10, 24, 25, 22]
# print(non_divisible_subset(4, arr))
# arr = [1, 7, 2, 4]
# print(non_divisible_subset(3, arr))
arr = [278, 576, 496, 727, 410, 124, 338,
       149, 209, 702, 282, 718, 771, 575, 436]
print(non_divisible_subset(7, arr))
