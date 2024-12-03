def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    left_list = []
    right_list = []
    for line in lines:
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)
    return left_list, right_list

def calculate_total_distance(left_list, right_list):
    left_list.sort()
    right_list.sort()
    total_distance = 0
    for left, right in zip(left_list, right_list):
        total_distance += abs(left - right)
    return total_distance

def calculate_similarity_score(left_list, right_list):
    similarity_score = 0
    for left in left_list:
        similarity_score += left * right_list.count(left)
    return similarity_score

left_list, right_list = read_input('day1/input.txt')
total_distance = calculate_total_distance(left_list, right_list)
print(f"Total Distance: {total_distance}")

similarity_score = calculate_similarity_score(left_list, right_list)
print(f"Similarity Score: {similarity_score}")
