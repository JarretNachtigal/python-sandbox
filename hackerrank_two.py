from collections import OrderedDict

# this answer works but is slow - o(n^2) or o(n*m)


def readFile(fileName):  # this was edited for this specific case, copy from rations.py for reusable one
    # opens the file in read mode
    fileObj = open(fileName, "r")
    words = fileObj.readlines()
    ranked = words[1].split()
    player = words[3].split()
    fileObj.close()
    i = 5
    arr = []
    while i < len(words):
        arr.append(int(words[i]))
        i += 1
    ranked = list(map(int, ranked))
    player = list(map(int, player))
    return ranked, player, arr


def difference(arr, arr_two):
    i = 0
    while i < len(arr):
        if not arr[i] == arr_two[i]:
            print("my answer: ", arr[i], "at index", i)
            print("their answer: ", arr_two[i], "at index", i)
        i += 1


def climbingLeaderboard(ranked, player):
    debug = True  # print statements if True
    # ranked is the leaderboard scores in an arr
    # player is a single player's scores

    player_leaderboard = []  # new array to return
    # remove duplicates from ranked
    new_ranked = list(OrderedDict.fromkeys(ranked))
    # loop through player
    i = 0
    while i < len(player):
        # inner loop will tell what place the score is in
        j = 0
        # find correct place in leaderboard for score at player[i]
        while new_ranked[j] > player[i] and j < len(new_ranked)-1:
            j += 1
        # if last place
        if j == len(new_ranked)-1 and player[i] < new_ranked[j]:
            j += 1
        player_leaderboard.append(j+1)
        i += 1
    # fill player_leaderboard
    i = 0
    return player_leaderboard


# o(n log n)?
def climbingLeaderboardTwo(ranked, player):
    debug = True  # debug prints if true
    player_leaderboard = []  # new array to return
    # remove duplicates from ranked
    new_ranked = list(OrderedDict.fromkeys(ranked))
    # find the index that each player[] item would be inserted into
    # append that to player_leaderboard
    # return player leaderboard
    for score in player:
        player_leaderboard.append(binary_search(new_ranked, score)+1)
    return player_leaderboard


# o(log n)
def binary_search(arr, item):
    begin_index = 0
    end_index = len(arr) - 1

    while begin_index <= end_index:
        midpoint = (begin_index + end_index) // 2
        midpoint_value = arr[midpoint]
        if midpoint_value == item:
            return midpoint
        elif item > midpoint_value:
            end_index = midpoint - 1
        else:
            begin_index = midpoint + 1
    return begin_index  # return insertion point


player = [5, 25, 50, 120]
ranked = [100, 100, 50, 40, 40, 20, 10]
my_ans = climbingLeaderboardTwo(ranked, player)
ans = [6, 4, 2, 1]
difference(my_ans, ans)

ranked, player, ans = readFile("climbing_leaderboard.txt")
my_ans = climbingLeaderboardTwo(ranked, player)
difference(my_ans, ans)
arr = [1, 2, 3, 4, 6, 7, 8, 9, 10]
