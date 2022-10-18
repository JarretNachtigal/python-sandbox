import os


def main():
    file_stuff()
    pass

# modes
# a = append
# r = read
# t = text
# defualt = "rt"
# w = write (overwrite)
# x = create (fails if exists)


def file_stuff():
    # create
    f = open("file.txt", "x")
    f.close()
    # overwrite
    f = open("file.txt", "w")
    f.write("things \nand\nstuff \n")
    f.close()
    # append
    f = open("file.txt", "a")
    f.write("and also more things \n")
    f.close()
    # read
    f = open("file.txt")
    print(f.read())
    # print(f.readline())
    f.close()
    # delete
    os.remove("file.txt")


if __name__ == "__main__":
    main()
