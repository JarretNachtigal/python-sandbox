# return the date of the day of the programmer (256th day of the year)
# based on russain calander - julian (1700-1917) and gregorian(post- jan 31st 1918) calanders
# in 1918 the day went from jan 31 - feb 14th
def dayOfTheProgrammer(year):
    # determine gregorian or julian calander - 1 is gregorian, 0 is julian
    calander_type = 0  # defualt julian
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # calander type
    if year > 1918:
        calander_type = 1
    # check for special case year - 1918
    if year == 1918:
        # handles day counter for special case year, needs to be specially formatted later?
        month_days[1] -= 13

    # determine leap year
    if calander_type == 1:
        if year % 4 == 0:
            if year % 100 != 0:
                print(year, "is a leap year")
                month_days[1] += 1
            elif year % 400 == 0:
                month_days[1] += 1
                print(year, "is a leap year")
    else:
        if year % 4 == 0:
            month_days[1] += 1
            print(year, "is a leap year")

    # determine month
    day_counter = 256  # day of the programmer
    i = 0
    while i < 11 and day_counter - month_days[i] > 0:
        # remove days from each month from day count
        day_counter -= month_days[i]
        print(day_counter)
        # increment
        i += 1
    month = i + 1  # i can be thought of as a month counter
    # determine day - days left in day counter is the day of the month
    day = day_counter
    # format output
    if month < 10:
        month = "0"+str(month)
    if day < 10:
        day = "0"+str(day)
    date = str(day)+"."+str(month)+"."+str(year)
    return date


print(dayOfTheProgrammer(1800))
print(dayOfTheProgrammer(2017))
print(dayOfTheProgrammer(2016))
print(dayOfTheProgrammer(1918))
