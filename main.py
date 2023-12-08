import day1_1 as d1a
import day1_2 as d1b
import day2_1 as d2a
import day2_2 as d2b
import day3_1 as d3a

def read_file(filename):
    with open(filename) as f:
        return f.read()

def write_file(filename, data):
    with open(filename, "w") as f:
        f.write(data)

def append_to_file(filename, data):
    with open(filename, "a") as f:
        f.write(data)



if __name__ == "__main__":
    file = read_file("input.txt")
    print("Input:")
    print(file)
    print("\nOutput:")
    touching_numbers = d3a.check_distance(d3a.create_matrix(file))
    print(touching_numbers)
    print(f"Sum of numbers: {d3a.sum_of_numbers(touching_numbers)}")