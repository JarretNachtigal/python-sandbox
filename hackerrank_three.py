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


# arr = []
# for i in range(0, 100):
#     arr.append(66)

# print(picking_numbers(arr))

def check_left_and_right(n, k, r_q, c_q, obstacles=[]):
    # obstacle dict with column => rows
    obstaclesDict = {}
    if k > 0:
        for row, column in obstacles:
            # if row exist, add column to its arr
            # else add row = [column]
            if not column in obstaclesDict:
                obstaclesDict[column] = [row]
            else:
                obstaclesDict[column].append(row)
    # from queen, left --------------
    count_left = 0
    i = c_q  # column of queen (not index)
    while i > 1:  # check from queen to left (0)
        if i-1 in obstaclesDict:  # if column i in obstacles
            if r_q in obstaclesDict[i-1]:  # if row in given column list
                break
            else:  # row is open
                count_left += 1
        else:
            count_left += 1
        i -= 1

    # from queen, right
    count_right = 0
    i = c_q  # column of queen (not index)
    while i < n:  # check from queen to right (n)
        if i+1 in obstaclesDict:  # if column i in obstacles
            if r_q in obstaclesDict[i+1]:  # if row in given column list
                break
            else:  # row is open
                count_right += 1
        else:
            count_right += 1
        i += 1
    print("right", count_right, "left", count_left)
    return count_right + count_left


def check_up_and_down(n, k, r_q, c_q, obstacles=[]):
    # obstacle dics with rows => [columns]
    obstaclesDict = {}  # locations
    if k > 1:
        for row, column in obstacles:
            # if row exist, add column to its arr
            # else add row = [column]
            if not row in obstaclesDict:
                obstaclesDict[row] = [column]
            else:
                obstaclesDict[row].append(column)

    # from queen, up -------------
    count_up = 0  # count the number of possible moves
    row = r_q  # row of the queen (not index)
    while row < n:  # check next from queen to top
        if row+1 in obstaclesDict:  # if row i in obstacles
            if c_q in obstaclesDict[row+1]:  # if column in given row list
                break
            else:  # column is open
                count_up += 1
        else:
            count_up += 1
        row += 1

    # from queen, down -------------
    count_down = 0
    i = r_q  # row of queen (not index)
    while i > 1:  # check next from queen to bottom
        if i - 1 in obstaclesDict:  # if row i in obstacles
            if c_q in obstaclesDict[i - 1]:  # if column in given row list
                break
            else:  # column is open
                count_down += 1
        else:
            count_down += 1
        # print(i)
        i -= 1
    print("up:", count_up, "down:", count_down)
    return count_up + count_down


def check_diagonals(n, k, r_q, c_q, obstacles=[]):
    # obstacle dics with rows => [columns]
    obstaclesDict = {}  # locations
    if k > 0:
        for row, column in obstacles:
            # if row exist, add column to its arr
            # else add row = [column]
            if not row in obstaclesDict:
                obstaclesDict[row] = [column]
            else:
                obstaclesDict[row].append(column)

    # from queen, diagonal up right ----------
    count_up_right = 0
    i = 1  # change row and column
    # check c_q + i, r_q + i while both are <= n
    while i + r_q <= n and i + c_q <= n:  # go until end of board
        if (r_q + i) in obstaclesDict:
            if (c_q + i) in obstaclesDict[(r_q + i)]:
                break
            else:
                count_up_right += 1
        else:
            count_up_right += 1
        i += 1
    # from queen, diagonal up left ----------
    count_up_left = 0
    i = 1  # change row and column
    # check c_q - i while greater than  0, r_q + i while less than n
    while i + r_q <= n and c_q - i > 0:
        if (r_q + i) in obstaclesDict:
            if (c_q - i) in obstaclesDict[(r_q + i)]:
                break
            else:
                count_up_left += 1
        else:
            count_up_left += 1
        i += 1
    # from queen, diagonal down right ----------
    count_down_right = 0
    i = 1  # change row and column
    # check c_q - i greater than 0, r_q + i <= n
    while r_q - i > 0 and i + c_q <= n:  # go until end of board
        if (r_q - i) in obstaclesDict:
            if (c_q + i) in obstaclesDict[(r_q - i)]:
                break
            else:
                count_down_right += 1
        else:
            count_down_right += 1
        i += 1
    # from queen, diagonal down left ----------
    count_down_left = 0
    i = 1  # change row and column
    # check c_q - i greater than 0, r_q + i <= n
    while r_q - i > 0 and c_q - i > 0:  # go until end of board
        if (r_q - i) in obstaclesDict:
            if (c_q - i) in obstaclesDict[(r_q - i)]:
                break
            else:
                count_down_left += 1
        else:
            count_down_left += 1
        i += 1
    print("up right", count_up_right, "up left", count_up_left,
          "down right", count_down_right, "down left", count_down_left)
    return count_up_right + count_up_left + count_down_right + count_down_left


def queensAttack(n, k, r_q, c_q, obstacles=[]):
    # Write your code here
    # n - number of rows and columns
    # k - number of obstacles on the board
    # r_q - row of queen's position
    # c_q - column of queen's position
    # obstacles, list of obstacles - 2d list
    # return number of spaces the queen can attack

    # count each direction bounded by n from queen's location
    # if reaching an obstacle, STOP
    if n == 1:
        return 0
    vertical = check_up_and_down(n, k, r_q, c_q, obstacles)
    horizontal = check_left_and_right(n, k, r_q, c_q, obstacles)
    diagonal = check_diagonals(n, k, r_q, c_q, obstacles)

    return horizontal + vertical + diagonal


# input
# 5 3
# 4 3
# 5 5
# 4 2
# 2 3
n = 5
k = 3
r_q = 4
c_q = 3
obstacles = [[5, 5], [4, 2], [2, 3]]
print(queensAttack(n, k, r_q, c_q, obstacles))
# horizontal => 2
# vertical => 2
# diagonal => 6
# output => 10

n = 4
k = 0
r_q = 4
c_q = 4
obstacles = []
print(queensAttack(n, k, r_q, c_q, obstacles))
# output => 9
