# kevin - starts with vowels
# stuart - starts with consonants
def minion_game(string):

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
    vowels = ["A", "E", "I", "O", 'U']
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
    consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M',
                  'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
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

    print("stuart substrings", substrings)
    print("stuart score", score)
    return score


# beginning with vowel
def get_kevin_score(string):
    substrings = get_vowel_substrings(string)
    score = 0
    string_length = len(string)
    # search for number of each substring occurances in string
    for substring in substrings:
        length = len(substring)
        i = 0
        while i + length < string_length:
            if substring == string[i:i+length]:
                score += 1
            i += 1
        print(substring, score)

    print("kevin substrings", substrings)
    print("kevin score", score)
    return score


# print(get_vowel_substrings("banana"))
# print(get_consonant_substrings("banana"))
print(minion_game("baananas"))
