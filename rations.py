# hackerrank
def fairRations(B):
    # impossible
    if len(B) <= 2:
        return "NO"
    i = 0
    loaves_given = 0
    while i < len(B) - 1:
        if not B[i] % 2 == 0:  # if current is odd
            if not B[i-1] % 2 == 0:  # if left is odd
                B[i] += 1
                B[i-1] += 1
                loaves_given += 2
            elif B[i-1] % 2 == 0:  # if left is even
                B[i] += 1
                B[i+1] += 1
                loaves_given += 2
        else:  # current is even
            pass
        i += 1

    if not all(element % 2 == 0 for element in B):
        loaves_given = "NO"
    return str(loaves_given)


def readFile(fileName):
    fileObj = open(fileName, "r")  # opens the file in read mode
    words = fileObj.read().split()  # puts the file into an array
    fileObj.close()
    return words


arr = readFile("rations.txt")
arr = list(map(int, arr))
print(fairRations(arr))
arr = [2, 3, 4, 5, 6, 7]
print(fairRations(arr))
arr = readFile("rations.txt")
