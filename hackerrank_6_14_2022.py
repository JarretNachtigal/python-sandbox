# 1 ------ String Split and Join ------

# input = input("input a sentance ")


# def split_and_join(str):
#     arr = str.split(" ")
#     str = "-".join(arr)
#     return str


# print(split_and_join(input))

# 2 ------ The Minion Game ------

# input = input()


def minion_game(string):
    string = string.lower()
    vowels = {"a": False, "e": False, "i": False, "o": False,
              "u": False}  # False - not used, string index - used
    # kevin - starts with vowels
    # stuart - starts with consonants

    # determine winner and return, default stuart
    stuart_score = get_stuart_score()
    winner_score = stuart_score
    winner = "Stuart"
    kevin_score = get_kevin_score()
    if stuart_score < kevin_score:
        winner = "Kevin"
        winner_score = kevin_score

    return f"{winner} {winner_score}"

# this method will be used to find Kevin's score
# this method will find all substring's of a given input string that start with vowels, nonrepeating


def get_vowel_substrings(string, vowels):
    used_vowels = []
    for index, letter in enumerate(string):
        # if letter is a vowel and is the first instance of that vowel
        if letter in vowels and vowels[letter] == False:
            vowels[letter] = index  # save index of first instace of each value
            used_vowels.append(letter)

# this method will be used to find Stuart's score
# this method will find all substring's of a given input string that start with consonants, nonrepeating


def get_consonants_substrings(string, vowels, used_vowels):
    pass

# beginning with consonant


def get_stuart_score():
    pass

# beginning with vowel


def get_kevin_score():
    pass


print(minion_game("banana"))
