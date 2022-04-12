
# 1 - Python/Basic Data Types/Tuples

# # given n number of integers
# n = int(input())
# integer_list = map(int, input().split())
# # create a tuple containing n integers - integer_tuple
# integer_tuple = tuple(integer_list) #go from map object to tuple
# # compute and print result of hash(integer_tuple)
# print(hash(integer_tuple))

# --------------------------------------------------------

# 2 - Python/Regex and Parsing/HTML Parser Part 1

from html.parser import HTMLParser
n = int(input())  # number of lines to parse

# create a subclass and override the handler methods


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        # attrs is a list of tuples
        length = len(attrs)
        # loop through list
        for i in range(length):
            # print inner tuple
            inner_length = len(attrs[i])
            # loop through fields in i
            for n in range(0, inner_length, 2):
                print("->", attrs[i][n], ">", attrs[i][n+1])

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        # attrs is a list of tuples
        length = len(attrs)
        # loop through list
        for i in range(length):
            # print inner tuple
            inner_length = len(attrs[i])
            # loop through fields in i
            for n in range(0, inner_length, 2):
                print("->", attrs[i][n], ">", attrs[i][n+1])


# instantiate the parser and feed it some HTML
parser = MyHTMLParser()
for _ in range(n):
    parser.feed(input())
parser.close()
