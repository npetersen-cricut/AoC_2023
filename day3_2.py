import math

def create_matrix(input):
    matrix = [list(line) for line in input.splitlines() if line]

    for row in matrix:
        print(row)

    return matrix

def find_gear_ratios(matrix):
    gear_ratios = []  # List to store all numbers

    # Iterate over the matrix
    for column in range(len(matrix)):
        row = 0
        while row < len(matrix[column]):
            if matrix[column][row].isdigit():
                # Start of a new number
                list_of_digits = []
                touching_star = False
                i = row
                while i < len(matrix[column]) and matrix[column][i].isdigit():
                    list_of_digits.append(matrix[column][i])

                    # Check the surrounding cells for a '*'
                    for di in range(-1, 2):
                        for dj in range(-1, 2):
                            if (0 <= column + di < len(matrix)) and (0 <= i + dj < len(matrix[column])):
                                if matrix[column + di][i + dj] == '*':
                                    # Check if the '*' is touching another number
                                    for dk in range(-1, 2):
                                        for dl in range(-1, 2):
                                            if (0 <= column + di + dk < len(matrix)) and (0 <= i + dj + dl < len(matrix[column + di + dk])):
                                                if matrix[column + di + dk][i + dj + dl].isdigit():
                                                    # If true, then log the coordinates of the original number and the found number, so they can be skipped later.
                                                    # This is to prevent the same number from being added to the list multiple times.
                                                    touching_star = True
                                                    # Collect the digits of the number touching the '*'
                                                    list_of_digits_star = []
                                                    m = i + dj + dl
                                                    n = column + di + dk
                                                    while m < len(matrix[n]) and matrix[n][m].isdigit():
                                                        if not (n == column and m == i):
                                                            list_of_digits_star.append(matrix[n][m])
                                                        m += 1
                                                    # Convert the list of digits to a number and add it to the list
                                                    if list_of_digits_star:
                                                        number_star = int(''.join(list_of_digits_star))
                                                        gear_ratios.append(number_star)
                    i += 1

                # Convert the list of digits to a number and add it to the list
                if list_of_digits and touching_star:
                    number = int(''.join(list_of_digits))
                    gear_ratios.append(number)

                row = i  # Update the outer loop's index
            else:
                row += 1

    return gear_ratios


