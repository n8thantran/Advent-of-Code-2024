def is_safe(report):
    increasing = True
    decreasing = True
    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]
        if diff < 1 or diff > 3:
            return False
        if diff > 0:
            decreasing = False
        if diff < 0:
            increasing = False
    return increasing or decreasing

def is_safe_with_dampener(report):
    if is_safe(report):
        return True
    for i in range(len(report)):
        new_report = report[:i] + report[i + 1:]
        if is_safe(new_report):
            return True
    return False

with open('day2/input.txt') as f:
    reports = [list(map(int, line.split())) for line in f]

safe_count = sum(1 for report in reports if is_safe(report))
safe_with_dampener_count = sum(1 for report in reports if is_safe_with_dampener(report))

print(f"Part 1: {safe_count}")
print(f"Part 2: {safe_with_dampener_count}")
