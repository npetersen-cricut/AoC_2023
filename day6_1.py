time = []
record_distance = []


def parse_input(input):
    for line in input.splitlines():
        key, values = line.split(":")
        if key == "Time":
            time = [int(value) for value in values.split()]
        elif key == "Distance":
            record_distance = [int(value) for value in values.split()]

def  calculate_speed_and_distance(time_held_down):
    speed = time_held_down
    distance = speed * time_held_down

