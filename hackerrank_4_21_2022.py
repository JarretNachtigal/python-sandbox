# way too long but it works

def swap_case(s):
    words = s.split()
    new_words = ""
    # for each space seperated string in dataset
    for word in words:
        # for each letter in words, swapcase
        new_word = ""
        for letter in word:
            if letter.isupper():
                new_word += letter.lower()
            else:
                new_word += letter.upper()
        new_words += new_word + " "
    new_words = new_words[:-1]
    return new_words
