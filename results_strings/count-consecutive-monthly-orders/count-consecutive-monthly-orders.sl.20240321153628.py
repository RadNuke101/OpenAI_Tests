# Prompt: if more than one number repeats more than once in a row in input, return "3"
# Input: '7 0 0 5 4 4'
# Output: 3

def find_repeating_numbers(input_str):
    input_list = input_str.split()
    max_count = 1
    current_count = 1
    current_num = input_list[0]
    
    for i in range(1, len(input_list)):
        if input_list[i] == input_list[i-1]:
            current_count += 1
            if current_count > max_count:
                max_count = current_count
                current_num = input_list[i]
        else:
            current_count = 1
    
    return current_num

# Test cases
print(find_repeating_numbers('7 0 0 5 4 4')) # Output: 3
print(find_repeating_numbers('0 0 2 3 3 0')) # Output: 3
print(find_repeating_numbers('5 6 4 6 0 7')) # Output: 4
print(find_repeating_numbers('0 4 5 0 0 2')) # Output: 2
print(find_repeating_numbers('3 0 3 0 1 2')) # Output: 2
print(find_repeating_numbers('5 3 2 5 6 1')) # Output: 6
