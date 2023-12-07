# Description: Day 2, Part 2 of Advent of Code 2023

from functools import reduce

def parse_input(input):
    """ Parse the input string and print the power values and their sum.

    Args:
        input (str): The input file as a string.
    """
    power_values = []

    for line in input.splitlines():

        # Split line into needed parts
        split_line = line.split(":")

        line_id = get_line_id(split_line[0])

        game_results = get_game_results(split_line[1])
        print(f"Game {line_id} results: {game_results}")

        max_values = find_max_values(game_results)
        power_values.append(power_the_dice(max_values))

    print(f"\nPower values: {power_values}")
    print(f"\nSum of power values: {sum(power_values)}")



def get_line_id(input):
    """Return the line ID from the line string."""
    return input.split(" ")[1]

def get_game_results(input):
    """Return the game results from the line string."""
    return input.split(";")

def power_the_dice(max_values):
    """Return the power of the dice."""
    return reduce(lambda x, y: x * y, max_values.values())

def find_max_values(game_results):
    """Return the max values for each color."""
    max_values = {}
    for game in game_results:
        values = [value.strip() for value in game.split(",")]
        values = [(value.split(" ")[1], int(value.split(" ")[0])) for value in values]

        for color, value in values:
            if color not in max_values or value > max_values[color]:
                max_values[color] = value
    print(f"Max values: {max_values}")
    return max_values
