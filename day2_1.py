# Description: Day 2, part 1 of Advent of Code 2023

# Constants
MAX_VALUES = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }

def parse_input(input):
    """Parse the input string and print possible games and their sum."""
    possible_games = []

    for line in input.splitlines():

        # Split line into needed parts
        split_line = line.split(":")

        line_id = get_line_id(split_line[0])

        game_results = get_game_results(split_line[1])
        print(f"Game {line_id} results: {game_results}")

        if is_game_possible(game_results):
            possible_games.append(int(line_id))

    print(f"Possible games: {possible_games}")
    print(f"Sum of possible game ids: {sum(possible_games)}")


def get_line_id(input):
    """Return the line ID from the line string."""
    return input.split(" ")[1]

def get_game_results(input):
    """Return the game results from the line string."""
    return input.split(";")

def is_game_possible(game_results):
    """Return True if all game results are within the max values, False otherwise."""
    for game in game_results:
        values = [value.strip() for value in game.split(",")]
        values = [(value.split(" ")[1], int(value.split(" ")[0])) for value in values]
        print(f"Values: {values}")
        for color, value in values:
            if int(value) > MAX_VALUES[color]:
                print(f"Value {value} is too high for color {color}")
                return False
    return True
