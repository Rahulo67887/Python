# Sample lists of lists
lists = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]

# Initialize variables to store the maximum sum and the corresponding list
max_sum = 0
max_list = 0

# Iterate through the lists
for sub_list in lists:
    current_sum = sum(sub_list)  # Calculate the sum of elements in the current list
    if current_sum > max_sum:
        max_sum = current_sum
        max_list = sub_list

# Print the list with the highest sum
print("List with the highest sum:", max_list)
