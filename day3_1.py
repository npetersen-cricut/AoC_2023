import math

def create_matrix(input):
    matrix = [list(line) for line in input.splitlines() if line]

    for row in matrix:
        print(row)

    return matrix


# Not actually using euclidean distance anymore to determine if a number is touching a symbol
def euclidean_distance(matrix):
    valid_numbers = []  # List to store all numbers

    # Iterate over the matrix
    for column in range(len(matrix)):
        row = 0
        while row < len(matrix[column]):
            if matrix[column][row].isdigit():
                # Start of a new number
                list_of_digits = []
                touching_symbol = False
                i = row
                while i < len(matrix[column]) and matrix[column][i].isdigit():
                    list_of_digits.append(matrix[column][i])

                    # Check the surrounding cells for a non-alphanumeric or non-dot character
                    for di in range(-1, 2):
                        for dj in range(-1, 2):
                            if (0 <= column + di < len(matrix)) and (0 <= i + dj < len(matrix[column])):
                                if not (matrix[column + di][i + dj].isalnum() or matrix[column + di][i + dj] == '.'):
                                    touching_symbol = True
                    i += 1

                # Convert the list of digits to a number and add it to the list
                if list_of_digits and touching_symbol:
                    number = int(''.join(list_of_digits))
                    valid_numbers.append(number)

                row = i  # Update the outer loop's index
            else:
                row += 1

    return valid_numbers

def sum_of_numbers(numbers):
    return sum(numbers)

