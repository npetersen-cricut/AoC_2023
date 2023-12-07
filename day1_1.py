
def find_numbers(input):
    list_of_digits = []

    for line in input.splitlines():
        first_digit = next((char for char in line if char.isdigit()), None)
        last_digit = next((char for char in reversed(line) if char.isdigit()), None)

        number = combine_digits(first_digit, last_digit)
        list_of_digits.append(sum_digits([number]))

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

