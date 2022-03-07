from collections import OrderedDict


def climbingLeaderboard(ranked, player):
    # Write your code here
    # ranked is the leaderboard scores in an arr
    # player is a single player's scores
    # new array to return
    player_leaderboard = []
    # remove duplicates from ranked
    new_ranked = list(OrderedDict.fromkeys(ranked))
    # loop through player
    i = 0
    while i < len(player):
        # inner loop will tell what place the score is in
        j = 0
        # find correct place in leaderboard for score at player[i]
        while new_ranked[j] > player[i] and j < len(new_ranked) - 1:
            j += 1
            print(j)
        if j == len(new_ranked)-1:
            j += 1
        player_leaderboard.append(j+1)
        i += 1
    print("player: ", player)
    print("new_ranked: ", new_ranked)
    # fill player_leaderboard
    i = 0
    return player_leaderboard


player = [5, 25, 50, 120]
ranked = [100, 100, 50, 40, 40, 20, 10]
print(climbingLeaderboard(ranked, player))
