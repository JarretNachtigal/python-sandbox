# 1 ------ String Split and Join ------

# input = input("input a sentance ")


# def split_and_join(str):
#     arr = str.split(" ")
#     str = "-".join(arr)
#     return str


# print(split_and_join(input))

# 2 ------ The Minion Game ------

# input = input()


# kevin - starts with vowels
# stuart - starts with consonants
def minion_game(string):
    # ignore uppercase
    string = string.lower()

    # determine winner and return, default stuart
    stuart_score = get_stuart_score(string)
    winner_score = stuart_score
    winner = "Stuart"
    kevin_score = get_kevin_score(string)
    # swap winner if needed
    if stuart_score < kevin_score:
        winner = "Kevin"
        winner_score = kevin_score

    return f"{winner} {winner_score}"


# this method will be used to find Kevin's score
# this method will find all substring's of a given input string that start with vowels, nonrepeating
def get_vowel_substrings(string):
    vowels = ["a", "e", "i", "o", 'u']
    substrings = []
    length = len(string)
    for letter in vowels:  # loop through vowels to check if they exist
        if string.count(letter) > 0:  # if they exist
            substrings.append(letter)  # add vowel to substrings
            i = string.index(letter) + 1  # set i to index of vowel + 1
            while i < length:  # add remaining substrings after the vowel
                # add previous substring + next letter
                substrings.append(substrings[len(substrings) - 1] + string[i])
                i += 1

    return substrings


def get_consonant_substrings(string):
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
                  'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    substrings = []
    length = len(string)
    for letter in consonants:  # loop through vowels to check if they exist
        if string.count(letter) > 0:  # if they exist
            substrings.append(letter)  # add vowel to substrings
            i = string.index(letter) + 1  # set i to index of vowel + 1
            while i < length:  # add remaining substrings after the vowel
                # add previous substring + next letter
                substrings.append(substrings[len(substrings) - 1] + string[i])
                i += 1

    return substrings


# beginning with consonant
def get_stuart_score(string):
    substrings = get_consonant_substrings(string)
    score = 0
    for substring in substrings:
        score += string.count(substring)

    return score


# beginning with vowel
def get_kevin_score(string):
    substrings = get_vowel_substrings(string)
    score = 0
    for substring in substrings:
        score += string.count(substring)

    return score


# print(get_vowel_substrings("banana"))
# print(get_consonant_substrings("banana"))
print(minion_game("banana"))
