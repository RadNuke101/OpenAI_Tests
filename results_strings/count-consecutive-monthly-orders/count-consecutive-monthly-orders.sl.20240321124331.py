# Prompt: if more than one number repeats more than once in a row in input, return "3"
# Input: '7 0 0 5 4 4'
# Output: 3

def find_repeated_numbers(input_str):
    nums = input_str.split()
    count = 1
    max_count = 1
    
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 1
    
    if max_count > 2:
        return '3'
    else:
        return str(max_count)

# Test cases
print(find_repeated_numbers('7 0 0 5 4 4'))  # Output: 3
print(find_repeated_numbers('0 0 2 3 3 0'))  # Output: 3
print(find_repeated_numbers('5 6 4 6 0 7'))  # Output: 4
print(find_repeated_numbers('0 4 5 0 0 2'))  # Output: 2
print(find_repeated_numbers('3 0 3 0 1 2'))  # Output: 2
print(find_repeated_numbers('5 3 2 5 6 1'))  # Output: 6
