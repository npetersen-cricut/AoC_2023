import day1_1 as d1a
import day1_2 as d1b
import day2_1 as d2a


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
    print(d2a.parse_input(file))
