def form_square(s):
    # find largest sum
    sums = []  # 3 horizontals top to bottom, 3 verticals left to right, 2 diagonals - left to right first
    # get into first layer
    for arr in s:
        sum = 0
       # ----- sum of horozontal -----
        for i in arr:
            sum += i
        # remember highest sum
        sums.append(sum)  # save sums
    # ----- sum of vertical -----
    i = 0
    while i < len(s):
        sum = 0
        j = 0
        while j < len(s):
            sum += s[j][i]
            j += 1
        # remember highest sum
        sums.append(sum)  # save sums
        i += 1
    # ----- sum of diagonals -----
    sums.append(s[0][0] + s[1][1] + s[2][2])
    sums.append(s[0][2] + s[1][1] + s[2][0])
    # ----- get largest/target number -----
    largest = max(sums)
    # check if each line adds to largest, change top left, then middle, then bottom right as needed?
    difference = 0  # this will hold sum of the changes in s
    for i in range(0, 3):
        # horizontal and vertical sums
        if not (sums[(0+i)] == largest and sums[(3+i)] == largest):
            # count numbers needed to change s[i][i] to make sum = largest
            difference += abs(sums[0+i] - largest)
    return difference


matrix = [[4, 9, 2],
          [3, 5, 7],
          [8, 1, 5]]
print("matrix: ", matrix)
print("output: ", form_square(matrix))
