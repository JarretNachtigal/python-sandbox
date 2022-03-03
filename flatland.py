import sys


def flatlandSpaceStations(n, c):
    # if there is only 1 space station, the farthest city will be
    # n -> number of cities (cities from 0 - n exist)
    # c[0] the num location of the only station
    # ex, 100 cities, station at 0
    # city 100 is 99km away from the station
    if n == 1:
        return n - 1
    c.sort()
    distance_from_prev = 0
    distance_from_next = 0
    current_distance = 0
    max_distance = 0
    station_index = 0
    prev_station = c[station_index]
    next_station = c[station_index + 1]
    i = 0
    while i < n:
        # get distances from prev and current stations
        distance_from_prev = abs(i - prev_station)
        distance_from_next = abs(i - next_station)
        if distance_from_next > distance_from_prev:
            current_distance = distance_from_prev
        else:
            current_distance = distance_from_next
        # save biggest difference
        if current_distance > max_distance:
            max_distance = current_distance
        # once station is reached, change prev and next, dont go out of bounds
        if i == next_station and not station_index == len(c) - 2:
            station_index += 1
            prev_station = c[station_index]
            next_station = c[station_index + 1]
        # iterate
        i += 1
    return max_distance

# works, but is way too slow o(n^2)


def flatlandSpaceStationsTwo(n, c):
    max_distance = 0
    i = 0
    while i < n:
        current_distance = sys.maxsize
        # check abs of all values in c with i

        for station in c:
            # remember closest value in c to i
            if abs(i - station) < current_distance:
                current_distance = abs(i - station)
            # print(i, " current distance: ",
            #       current_distance, "station: ", station)
        i += 1
        if current_distance > max_distance:
            max_distance = current_distance
    # save the highest
    return max_distance


n = 6
arr = [0, 1, 2, 3, 4, 5]
print(flatlandSpaceStations(n, arr))
n = 20
arr = [13, 1, 11, 10, 6]
print(flatlandSpaceStations(n, arr))
n = 1
arr = [0]
print(flatlandSpaceStations(n, arr))
# n = 6
# arr = [0, 1, 2, 3, 4, 5]
# print(flatlandSpaceStationsTwo(n, arr))  # => 0
# n = 20
# arr = [13, 1, 11, 10, 6]
# print(flatlandSpaceStationsTwo(n, arr))  # => 6
