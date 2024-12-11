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

# specify our file path with the lists
file_path = "puzzle-input.txt"

left_list, right_list = read_lists_from_file(file_path)

result = find_difference_between_lists(left_list, right_list)

print(f"Difference: {result}")
