"""
This module contains functions for parsing input data into a direction pattern and a dictionary of nodes,
and for transiting the nodes based on the direction pattern.

The main function is `main()`, which takes a string of input data, parses it into a direction pattern and a dictionary of nodes,
transits the nodes based on the direction pattern, and prints the final node and the number of steps.
"""

from collections import namedtuple
from typing import Dict, Tuple

Connection = namedtuple('Connection', ['left', 'right'])

def main(input_data: str) -> None:
    """Main function that parses the input and transits the nodes.

    Args:
        input_data (str): Should include the direction pattern and a list of nodes with connections.
    """
    direction_pattern, nodes = parse_input(input_data)
    final_node, number_of_steps = transit_nodes(direction_pattern, nodes)
    print(f"Final node: {final_node}")
    print(f"Number of steps: {number_of_steps}")

def parse_input(input: str) -> Tuple[str, Dict[str, Connection]]:
    """Parses the input data into a direction pattern and a dictionary of nodes.

    Args:
        input (str): The input data.

    Returns:
        Tuple[str, Dict[str, Connection]]: Returns a tuple containing the direction pattern and a dictionary of nodes.
    """
    lines = input.splitlines()
    direction_pattern = lines[0]
    print(f"Direction pattern length: {len(direction_pattern)}")
    nodes = {}

    for line in lines[2:]:
        node, values = line.split("=")
        values = values.replace('(', '').replace(')', '')
        left, right = values.split(',')
        nodes[node.strip()] = Connection(left.strip(), right.strip())

    # print(f"nodes: {nodes}")
    return direction_pattern, nodes


def transit_nodes(direction_pattern: str, nodes: Dict[str, Connection]) -> Tuple[str, int]:
    """Transits the nodes based on the direction pattern.

    Args:
        direction_pattern (str): A string containing the direction pattern.
        nodes (Dict[str, Connection]): A list of nodes with connections.

    Returns:
        Tuple[str, int]: The final node and the total number of steps taken.
    """
    current_node = 'AAA'
    pattern_index = 0

    while current_node != 'ZZZ':
        direction = direction_pattern[pattern_index % len(direction_pattern)]
        if direction == 'L':
            current_node = nodes[current_node].left
        else:
            current_node = nodes[current_node].right
        pattern_index += 1

    return current_node, pattern_index


