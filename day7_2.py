from collections import Counter
from typing import Dict, List, Tuple

CARD_VALUES = {str(i): i for i in range(2, 10)}
CARD_VALUES.update({'T': 10, 'J': 1, 'Q': 12, 'K': 13, 'A': 14})

def parse_input(input):
    hands = []
    for line in input.splitlines():
        hand, bid = line.split()
        value = read_hand(hand)
        print(f"Hand: {hand}, Bid: {bid}, Value: {value}")
        hands.append([hand, int(bid), int(value)])

    print(f"Hands: {hands}")
    sorted_hands = sort_hands(hands)
    print(f"Sorted Hands: {sorted_hands}")
    values = get_values(sorted_hands)
    print(f"Values: {values}")
    print(f"Sum of values: {sum(values)}")

def read_hand(string: str) -> int:
    char_counts = Counter(string)
    print(f"Char counts: {char_counts}")

    char_counts = new_joker_rule(char_counts)

    # Sort values in descending order
    sorted_counts = sorted(char_counts.values(), reverse=True)
    max_count = sorted_counts[0]
    return determine_hand_value(max_count, sorted_counts)

def new_joker_rule(counts: Dict[str, int]) -> Dict[str, int]:
    """
    Apply the new joker rule to the counts dictionary.

    Args:
        counts (dict): A dictionary containing counts of different keys.

    Returns:
        dict: The updated counts dictionary.
    """
    if 'J' in counts and counts.keys() - {'J'}:
        # Get the key with the highest value that is not 'J' (avoiding problems when all 'J')
        max_key = max((k for k in counts.keys() if k != 'J'), key=counts.get)
        # Add the value of J to the value of max_key and remove from dict.
        counts[max_key] += counts.pop('J')
    return counts


def determine_hand_value(max_count: int, sorted_counts: List[int]) -> int:
    print(f"Sorted counts: {sorted_counts}, Max count: {max_count}")
    if max_count == 1:
        return 0
    elif 1 < max_count < 3:
        return 2 if sorted_counts[1] == 2 else 1
    elif max_count == 3:
        return 4 if sorted_counts[1] == 2 else 3
    elif 4 <= max_count <= 5:
        return max_count + 1

def sort_hands(hands: List[Tuple[str, int, int]]) -> List[Tuple[str, int, int]]:
    # Sort hands based on the third value and the card values
    sorted_hands = sorted(hands, key=lambda x: (x[2], [CARD_VALUES[card] for card in x[0]]))
    return sorted_hands

def get_values(sorted_hands: List[Tuple[str, int, int]]) -> List[int]:
    return [hand[1] * (index + 1) for index, hand in enumerate(sorted_hands)]






