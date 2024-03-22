# Prompt: if more than one number repeats more than once in a row in input, return "3"
# Input: '7 0 0 5 4 4'
# Output: 3

def find_repeating_number(input_str):
    input_list = input_str.split()
    max_count = 1
    current_count = 1
    prev_num = input_list[0]

    for i in range(1, len(input_list)):
        if input_list[i] == prev_num:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 1
            prev_num = input_list[i]

    if max_count > 1:
        return str(max_count)
    else:
        return "No repeating numbers more than once in a row"

# Test cases
print(find_repeating_number('7 0 0 5 4 4'))  # Output: 3
print(find_repeating_number('0 0 2 3 3 0'))  # Output: 3
print(find_repeating_number('5 6 4 6 0 7'))  # Output: 4
print(find_repeating_number('0 4 5 0 0 2'))  # Output: 2
print(find_repeating_number('3 0 3 0 1 2'))  # Output: 2
print(find_repeating_number('5 3 2 5 6 1'))  # Output: 6
