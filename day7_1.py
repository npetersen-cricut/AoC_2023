from collections import Counter

def parse_input(input):
    hands = []
    for line in input.splitlines():
        hand, bid = line.split()
        value = read_hand(hand)
        print(f"Hand: {hand}, Bid: {bid}, Value: {value}")
        hands.append([hand, int(bid), int(value)])

    # print(f"Hands: {hands}")
    sorted_hands = sort_hands(hands)
    # print(f"Sorted Hands: {sorted_hands}")
    values = get_values(sorted_hands)
    # print(f"Values: {values}")
    print(f"Sum of values: {sum(values)}")

def read_hand(string):
    char_counts = Counter(string)

    # Sort values in descending order
    sorted_counts = sorted(char_counts.values(), reverse=True)
    max_count = sorted_counts[0]
    return determine_hand_value(max_count, sorted_counts)


def determine_hand_value(max_count, sorted_counts):
    # print(f"Sorted counts: {sorted_counts}, Max count: {max_count}")
    if max_count == 1:
        return 0
    elif 1 < max_count < 3:
        return 2 if sorted_counts[1] == 2 else 1
    elif max_count == 3:
        return 4 if sorted_counts[1] == 2 else 3
    elif 4 <= max_count <= 5:
        return max_count + 1

def sort_hands(hands):
    # Map card characters to their corresponding values
    card_values = {str(i): i for i in range(2, 10)}
    card_values.update({'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14})

    # Sort hands based on the third value and the card values
    sorted_hands = sorted(hands, key=lambda x: (x[2], [card_values[card] for card in x[0]]), reverse=False)
    return sorted_hands

def get_values(sorted_hands):
    values = []
    for index, hand in enumerate(sorted_hands):
        values.append(hand[1] * (index + 1))
    return values






