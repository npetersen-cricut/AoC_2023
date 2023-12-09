
def parse_input(input):
    card_values = []
    for line in input.splitlines():

        card_number_raw, puzzle_input = line.split(":")
        winning_numbers, your_numbers = puzzle_input.split("|")

        card_number = get_card_number(card_number_raw)

        winning_numbers = [int(num) for num in winning_numbers.split()]
        your_numbers = [int(num) for num in your_numbers.split()]

        number_of_winning_numbers = 0
        value_of_card = 0
        for number in your_numbers:
            if number in winning_numbers:
                number_of_winning_numbers += 1

        value_of_card = calculate_score(number_of_winning_numbers)
        card_values.append(value_of_card)

        print(f"Card number {card_number} has {number_of_winning_numbers} winning numbers and is worth {value_of_card} points!")
    print(f"Total score: {sum(card_values)}")

def get_card_number(raw_card_number):
    return int(raw_card_number.split()[1])

def calculate_score(number_of_matches):
    if number_of_matches > 0:
        return 2 ** (number_of_matches - 1)
    else:
        return 0