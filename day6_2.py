from functools import reduce
import operator

time_limits = []
record_distances = []
number_of_ways_to_win = []


def parse_input(input):
    for line in input.splitlines():
        if not line.startswith("#"):
            key, values = line.split(":")
            if key == "Time":
                max_times = [int(value) for value in values.split()]
            elif key == "Distance":
                record_distance = [int(value) for value in values.split()]
    max_times = squish_input(max_times)
    record_distance = squish_input(record_distance)
    find_times(max_times, record_distance)

def squish_input(input):
    number_str = ''.join(map(str, input))
    number = int(number_str)
    return number


def  calculate_speed_and_distance(time_held_down, total_time):
    speed = time_held_down
    distance = speed * (total_time - time_held_down)
    # print(f"Time held down: {time_held_down} seconds, Distance traveled: {distance} meters")
    return distance

# For each, calculate the speed and distance for 1, then range to max.
# For each, calculate the distance for the max time held down.

def calculate_all(time_allowed, record_distance):
    winning_strategies = []
    for time in range(time_allowed):
        distance = calculate_speed_and_distance(time, time_allowed)
        if distance > record_distance:
            winning_strategies.append(time)
    number_of_ways_to_win.append(len(winning_strategies))


def find_times(allowed_time, record_distance):

    print(f"\nTime allowed: {allowed_time} seconds, Record distance: {record_distance} meters")
    calculate_all(allowed_time, record_distance)
    print(f"\nNumber of ways to win: {number_of_ways_to_win}")

    product_of_ways_to_win = reduce(operator.mul, number_of_ways_to_win)
    print(f"Product of ways to win: {product_of_ways_to_win}")

