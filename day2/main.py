def is_safe(levels):
    increasing = True
    decreasing = True
    for i in range(len(levels) - 1):
        if not (1 <= levels[i+1] - levels[i] <= 3):
            increasing = False
        if not (1 <= levels[i] - levels[i+1] <= 3):
            decreasing = False
    return increasing or decreasing

def partOne():
    safe = 0
    with open('day2/input.txt', 'r') as file:
        lines = file.readlines()

    for line in lines:
        line = line.split()
        levels = [int(x) for x in line]
        if is_safe(levels):
            safe += 1
    return safe

def partTwo():
    safe = 0
    with open('day2/input.txt', 'r') as file:
        lines = file.readlines()

    for line in lines:
        line = line.split()
        levels = [int(x) for x in line]
        if is_safe(levels):
            safe += 1
        else:
            for i in range(len(levels)):
                new_levels = levels[:i] + levels[i+1:]
                if is_safe(new_levels):
                    safe += 1
                    break
    return safe

print(partOne())
print(partTwo())