"""
This module contains functions for parsing input data into a direction pattern and a dictionary of nodes,
and for transiting the nodes based on the direction pattern.

The main function is `main()`, which takes a string of input data, parses it into a direction pattern and a dictionary of nodes,
transits the nodes based on the direction pattern, and prints the final node and the number of steps.
"""

from collections import namedtuple
from typing import Dict, Tuple, List

Connection = namedtuple('Connection', ['left', 'right'])

def main(input_data: str) -> None:
    """Main function that parses the input and transits the nodes."""
    direction_pattern, nodes = parse_input(input_data)
    end_nodes_list = transit_nodes(direction_pattern, nodes)

    final_nodes = [node for node, _ in end_nodes_list]
    number_of_steps = end_nodes_list[0][1]

    print(f"Final nodes: {final_nodes}")
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


def transit_nodes(direction_pattern: str, nodes: Dict[str, Connection]) -> List[Tuple[str, int]]:
    """Transits the nodes based on the direction pattern."""

    # Get a list of the starting nodes
    current_nodes = [node for node in nodes if node.endswith('A')]
    pattern_indices = [0] * len(current_nodes)

    while not all (node.endswith('Z') for node in current_nodes):
        for index, current_node in enumerate(current_nodes):
            direction = direction_pattern[pattern_indices[index] % len(direction_pattern)]
            if direction == 'L':
                current_nodes[index] = nodes[current_node].left
            else:
                current_nodes[index] = nodes[current_node].right
            pattern_indices[index] += 1
        if pattern_indices[0] % 1000:
            print(f"Pattern indices: {pattern_indices}")

    if not check_pattern_indices(pattern_indices):
        raise ValueError("Pattern indices are not all the same.")

    return list(zip(current_nodes, pattern_indices))


def check_pattern_indices(pattern_indicies: List[int]) -> bool:
    """Check if the pattern indices are all the same."""
    return all(x == pattern_indicies[0] for x in pattern_indicies)
