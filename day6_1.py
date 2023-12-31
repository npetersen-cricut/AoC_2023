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
    find_times(max_times, record_distance)

def  calculate_speed_and_distance(time_held_down, total_time):
    speed = time_held_down
    distance = speed * (total_time - time_held_down)
    print(f"Time held down: {time_held_down} seconds, Distance traveled: {distance} meters")
    return distance

# For each, calculate the speed and distance for 1, then range to max.
# For each, calculate the distance for the max time held down.

def calculate_all(time_allowed, record_distance):
    winning_strategies = []
    for time in range(time_allowed):
        distance = calculate_speed_and_distance(time, time_allowed)
        if distance > record_distance:
            winning_strategies.append(time)
    print(f"Winning strategies: {winning_strategies}")
    number_of_ways_to_win.append(len(winning_strategies))


def find_times(allowed_time, record_distance):
    for i, time in enumerate(allowed_time):
        print(f"\nTime allowed: {time} seconds, Record distance: {record_distance[i]} meters")
        calculate_all(time, record_distance[i])
    print(f"\nNumber of ways to win: {number_of_ways_to_win}")

    product_of_ways_to_win = reduce(operator.mul, number_of_ways_to_win)
    print(f"Product of ways to win: {product_of_ways_to_win}")

