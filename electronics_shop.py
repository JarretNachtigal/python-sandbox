# hackerrank, this solution kinda sucks
def getMoneySpent(keyboards, drives, b):
    # fill dictonary with keyboard prices => b - keyboard prices
    keyboard_price_remainders = {}
    for keyboard_price in keyboards:
        keyboard_price_remainders[keyboard_price] = b - keyboard_price
    # look for highest value in drives that are low enough to afford
    highest_price_of_both = -1  # return value, never changes if nothing can be afforded
    for keyboard in keyboard_price_remainders:
        i = 0  # iterates through drives[] with keyboard_price_remainders{}
        while i < len(drives):
            # check if each keyboard and drive can be afforded
            if keyboard_price_remainders[keyboard] - drives[i] >= 0:
                # choose most expensive option for both
                if highest_price_of_both < keyboard + drives[i]:
                    highest_price_of_both = keyboard + drives[i]
                    # print(highest_price_of_both)
            i += 1  # increment
    # return cost of both if can be purchased
    # return -1 if both items cannot be purchased
    return highest_price_of_both


keyboards = [40, 50, 60]
drives = [5, 8, 12]
print(getMoneySpent(keyboards, drives, 60))
