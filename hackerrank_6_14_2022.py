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
              "u": False, "y": False}  # False - not used, string index - used
    used_vowels = []
    # kevin - starts with vowels
    # stuart - starts with consonants
    for index, letter in enumerate(string):
        # if letter is a vowel and is the first instance of that vowel
        if letter in vowels and vowels[letter] == False:
            vowels[letter] = index  # save index of first instace of each value
            used_vowels.append(letter)
    # find substrings starting with each vowel
    for letter in used_vowels:
        pass

    # compare each subtring with string S and give points

    # 1 point per substring instance
    return vowels


print(minion_game("banana"))
