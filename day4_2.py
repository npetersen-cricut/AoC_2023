
def parse_input(input):
    card_values = []
    for line in input.splitlines():

        card_number_raw, puzzle_input = line.split(":")
        winning_numbers, your_numbers = puzzle_input.split("|")

        card_number = get_card_number(card_number_raw)

        winning_numbers = [int(num) for num in winning_numbers.split()]
        your_numbers = [int(num) for num in your_numbers.split()]

        number_of_winning_numbers = 0
        for number in your_numbers:
            if number in winning_numbers:
                number_of_winning_numbers += 1

        card_values.append([number_of_winning_numbers, 1])

        print(f"Card number {card_number} has {number_of_winning_numbers} winning numbers.")
    calculate_cards(card_values)
    print(card_values)
    print(f"Total number of cards: {calculate_total_number_of_cards(card_values)}")

def get_card_number(raw_card_number):
    return int(raw_card_number.split()[1])

def calculate_cards(card_values):
    for index, card in enumerate(card_values):
        number_of_matches = card[0]
        number_of_cards = card[1]
        if number_of_matches > 0:
            for _ in range(number_of_cards):
                for i in range(number_of_matches):
                    card_values[index + 1 + i][1] += 1

def calculate_total_number_of_cards(card_values):
    total_number_of_cards = 0
    for card in card_values:
        total_number_of_cards += card[1]
    return total_number_of_cards
