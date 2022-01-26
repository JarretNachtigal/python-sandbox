import math

# variables ------

# world = "world"
# snake_case = True               # True or False (case sensitive)
# num = 1
# num += 1                        # add 1 to num
# float_num = 20.5
# print(type(world))              # print data type # output: "<class 'str'>"
# print(type(snake_case))         # print data type # output: "<class 'bool'>"
# print(type(num))                # print data type # output: "<class 'int'>"
# print(type(float_num))          # output: "<class 'float'>"
# print("hello " + world)         # output: hello world
# print("num is " + str(num))     # concatenate int


# multiple assignment ------

# name = "Bro"
# age = 21
# attractive = True
# # or
# name, age, attractive = "bro", 21, True
# print(name)
# print(age)
# print(attractive)

# in the case where all are the same

# Spongebob = Patrick = Sandy = Squidward = 30
# print(Spongebob)

# String methods ------

# name = "gamer"
# print(len(name))                  # prints 5
# print(name.find("a"))             # prints 1
# print(name.capitalize())          # prints Gamer (g is capitalized)
# print(name.capitalize)            # prints a memory address
# print(name.lower())
# print(name.upper())
# print(name.isdigit())
# # bool, check string contains only letters, output: True
# print(name.isalpha())
# print(name.count("a"))            # 1
# print(name.replace("g", "G"))     # Gamer
# print(name * 3)                   # gamergamergamer


# type casting ------

# x = 1
# y = 2.0
# z = "3"
# x = str(x)                          # 1 becomes "1"
# print(type(x))
# print(int(y))
# print(float(z))
# print(bool(x))                      # output: true

# user input ------

# name = input("what is your name? ")   # defaults to string
# age = int(input("how old are you? "))
# print("hello " + name)
# print("age + 1 = " + str(age + 1))

# math functions ------

# pi = 3.14
# print(round(pi))              # round to nearest int output: 3
# print(math.ceil(pi))          # round up output: 4
# print(math.floor(pi))         # round down output: 3
# print(abs(pi))                # absolute value output 3.14
# print(pow(pi, 2))             # exponent output: 9.8596
# print(math.sqrt(4))           # square route output: 2
# print(max(4, 5, 6))           # square route output: 6
# print(min(4, 5, 6))           # square route output: 4

# string slicing ------

# name = "Jarret Nachtigal"
# first_letter = name[0]
# # starting index inclusive, ending index noninclusive
# first_name = name[0:6]
# last_name = name[7:]            # skip space at [6], go to end
# thing = name[::2]               # step default 1 (every 2)
# print(first_letter)
# print(first_name)
# print(last_name)
# print(thing)                     # JaRrEt nAcHtIgAl - output: Jre ahia

# site = "http://google.com"
# # slice object
# slice = slice(7, -4)              # cut off http:// and .com
# print(site[slice])

# if else ------

# age = int(input("how old are you? "))

# if age > 21:
#     print("you can drink")
# elif age > 18:
#     print("you are an adult")
# elif age == 1:
#     print("you are 1")
# elif age < 0:
#     print("you havent been born yet")
# else:
#     print("you are a child")

# logical operators ------

# temp = int(input("what is the temperature outside?: "))

# if temp >= 0 and temp <= 30:
#     print("the temperature is good today")
# elif not(temp > 0) or temp > 30:                # not reverses the truthy/falsy value
#     print("the temperature is bad today")

# while loop ------

# thing = 1
# while thing <= 50:
#     print(thing)
#     thing += 1
# print("done")

# # loop continues until input is given
# name = ""
# while len(name) == 0:
#     name = input("what is your name?: ")

# for loop ------

for i in range(10):
    print(i)
