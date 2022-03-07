from collections import OrderedDict


def climbingLeaderboard(ranked, player):
    # Write your code here
    # ranked is the leaderboard scores in an arr
    # player is a single player's scores
    # new array to return
    player_leaderboard = []
    # remove duplicates from ranked
    new_ranked = list(OrderedDict.fromkeys(ranked))
    # print(new_ranked)
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


def readFile(fileName):
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
            print("my answer: ", arr[i], i)
            print("their answer: ", arr_two[i], i)
        i += 1


player = [5, 25, 50, 120]
ranked = [100, 100, 50, 40, 40, 20, 10]
my_ans = climbingLeaderboard(ranked, player)
ans = [6, 4, 2, 1]
difference(my_ans, ans)

ranked, player, ans = readFile("climbing_leaderboard.txt")
my_ans = climbingLeaderboard(ranked, player)
difference(my_ans, ans)
