from collections import Counter

def read_lists_from_file(file_path):
    left_list = []
    right_list = []

    # open and read the file line by line
    with open(file_path, "r") as file:
        for line in file:
            # split the line into two parts and convert to integers
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)

    return left_list, right_list

def find_difference_between_lists(left_list, right_list):
    # sort the two lists in ascending order
    left_list.sort()
    right_list.sort()

    # compute the total distance in a clear but concise way, without creating temp variables
    return sum(abs(a - b) for a, b in zip(left_list, right_list))

def calculate_similarity_score(left_list, right_list):
    # to calculate similarity score, we can use Counter, which counts the number of occurrences of a number in
    # a list and creates a dictionary type object, where the keys are the numbers from the list and the values
    # are their counts

    right_list_counts = Counter(right_list)

    # for each number in the left list, we will multiply it by its count in the right list and then add up the total
    similarity_score = sum(num * right_list_counts[num] for num in left_list)

    return similarity_score

# specify our file path with the lists
file_path = "day-1-input.txt"

left_list, right_list = read_lists_from_file(file_path)

result = find_difference_between_lists(left_list, right_list)

print(f"Difference: {result}")

similarity_score = calculate_similarity_score(left_list, right_list)

print(f"Similarity score: {similarity_score}")
