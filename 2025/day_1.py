def split_instruction(instruction):
    direction = list(instruction)[0]
    magnitude = int(instruction[1:])

    return direction, magnitude

def spin_left(curr, magnitude):
    if curr < magnitude:
        next = 100 - (magnitude - curr)
    else:
        next = curr - magnitude
    return next

def spin_right(curr, magnitude):
    if curr > (100 - magnitude):
        next = magnitude - (100 - curr)
    else:
        next = curr + magnitude
    if next == 100:
        next = 0
    return next

def update_number(curr, instruction):
    direction, magnitude = split_instruction(instruction)
    if direction == "L":
        next = spin_left(curr, magnitude)
    else:
        next = spin_right(curr, magnitude)
    return next

def update_score(next):
    if int(next) == 0:
        return 1
    else:
        return 0

def return_zero_count(directions):
    curr = 50
    score = 0
    for direction in directions:
        print(curr)
        curr = update_number(curr, direction)
        score += update_score(curr)
    return score

file_path = '2025/day_1_input.txt'
lines = []
with open(file_path, 'r') as file:
    for line in file:
        lines.append(line.strip())

print("Result: ", return_zero_count(lines))