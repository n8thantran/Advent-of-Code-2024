import re

def partOne(memory):
    total_sum = 0

    instructions = re.findall(r"mul\(\d+,\d+\)", memory)

    for instruction in instructions:
        x, y = map(int, re.findall(r"\d+", instruction))
        total_sum += x * y

    return total_sum

def partTwo(memory):
    enabled = True
    total_sum = 0

    instructions = re.findall(r"(mul\(\d+,\d+\)|do\(\)|don't\(\))", memory)

    for instruction in instructions:
        if instruction.startswith("mul("):
            if enabled:
                x, y = map(int, re.findall(r"\d+", instruction))
                total_sum += x * y
        elif instruction == "do()":
            enabled = True
        elif instruction == "don't()":
            enabled = False

    return total_sum

with open("day3/input.txt", "r") as file:
    memory = file.read()

print(partOne(memory))
print(partTwo(memory))
