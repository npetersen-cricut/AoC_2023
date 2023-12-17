import day1_1 as d1a
import day1_2 as d1b
import day2_1 as d2a
import day2_2 as d2b
import day3_1 as d3a
import day3_2 as d3b
import day4_1 as d4a
import day4_2 as d4b
import day6_1 as d6a
import day6_2 as d6b

def read_file(filename):
    with open(filename) as f:
        return f.read()

def write_file(filename, data):
    with open(filename, "w") as f:
        f.write(data)

def append_to_file(filename, data):
    with open(filename, "a") as f:
        f.write(data)


# Day 3 Part 2
# if __name__ == "__main__":
#     file = read_file("input.txt")
#     print("Input:")
#     print(file)
#     print("\nOutput:")
#     touching_numbers = d3b.find_gear_ratios(d3b.create_matrix(file))
#     print(touching_numbers)

if __name__ == "__main__":
    file = read_file("input.txt")
    print("Input:")
    print(file)
    print("\nOutput:")
    d6b.parse_input(file)