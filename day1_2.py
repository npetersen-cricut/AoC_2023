import re


def find_numbers(input):

    # Included digits to skip step of checking for digits.
    spelled_numbers = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        '1': '1',
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '5',
        '6': '6',
        '7': '7',
        '8': '8',
        '9': '9'
    }
    list_of_digits = []

    for line in input.splitlines():
        print(f"line: {line}")

        # bastards like this => 62xvvkpbhhbthreetwooneeightwozr
        # Find all spelled numbers in the line along with their starting index
        found_spelled_numbers = [(m.start(), word) for word in spelled_numbers for m in re.finditer(word, line)]
        print(f"Found spelled numbers: {found_spelled_numbers}")

        # Sort the list of tuples by the starting index
        sorted_spelled_numbers = sorted(found_spelled_numbers, key=lambda x: x[0])
        print(f"Sorted spelled numbers: {sorted_spelled_numbers}")

        # Get the digits from the spelled numbers
        digits_in_line = []
        for _, word in sorted_spelled_numbers:
            digits_in_line.append(int(spelled_numbers[word]))
        print(f"Digits in line: {digits_in_line}")

        # Finally, get the first and last digits
        first_digit = None
        last_digit = None
        if len(sorted_spelled_numbers) >= 1:
            first_digit = digits_in_line[0]
            last_digit = digits_in_line[-1]

        # In memorium of the wrong path...

        # for _, word in sorted_spelled_numbers:
        #     digit = spelled_numbers[word]
        #     line = line.replace(word, digit, 1)
        # print(f"Modified line: {line}")

        final_number = combine_digits(first_digit, last_digit)
        print(final_number)
        list_of_digits.append(sum_digits([final_number]))

    print(list_of_digits)
    return sum(list_of_digits)


def combine_digits(first, second):
    if first is not None and second is not None:
        return int(str(first) + str(second))
    else:
        print("One or both digits are None")
        return 0

def sum_digits(list_of_digits):
    return sum(list_of_digits)

