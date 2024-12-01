left = []
right = []

with open('day1/input.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    numbers = line.split()
    left.append(int(numbers[0]))
    right.append(int(numbers[1]))

def partOne():
    left.sort()
    right.sort()

    total_distance = 0

    for i in range(len(left)):
        total_distance += abs(left[i] - right[i])

    print(total_distance)

def partTwo():
    dicc1 = {}

    for num in right:
        if num not in dicc1:
            dicc1[num] = 0
        dicc1[num] += 1
    
    score = 0
    for num in left:
        if num in dicc1:
            score += num * dicc1[num]
    return score

print(partTwo())