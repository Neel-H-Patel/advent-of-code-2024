from typing import List


# function that determines if a report meets the criteria as "safe"
def is_safe(report: List[int]) -> bool:
    # check the make sure that the report meets the criteria of gradually increasing or gradually decreasing by 1 to 3
    increasing = all(1 <= report[i + 1] - report[i] <= 3 for i in range(len(report) - 1))
    decreasing = all(1 <= report[i] - report[i + 1] <= 3 for i in range(len(report) - 1))

    return increasing or decreasing

# function that loops through all reports and counts the number of safe ones
def count_safe_reports(filename: str) -> int:
    count = 0

    with open(filename) as file:
        for line in file:
            # split each line into a list of ints
            report = list(map(int, line.split()))
            if is_safe(report):
                count += 1

    return count

filename = "day-2-input.txt"

num_safe_reports = count_safe_reports(filename)
print(f"Number of safe reports: {num_safe_reports}")
