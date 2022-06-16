def utopianTree(n):
    # n = # of growth cycles / years
    # each spring height *= 2
    # each summer height += 1 meter
    # initial height = 1
    # return height after n cycles
    height = 1
    i = 0
    while i < n:
        height *= 2
        i += 1
        if i < n:
            height += 1
        i += 1
    return height


def hurdleRace(k, height):
    # k = character's natural jump height
    # if the character can already jump them, return 0
    # find difference between max(height) and k
    # return it
    difference = max(height) - k
    if difference < 1:
        return 0
    return difference
