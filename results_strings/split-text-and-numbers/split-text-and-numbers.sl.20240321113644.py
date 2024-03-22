# Prompt: remove numbers from first input
# Input: ['apples30', '7'] 
# Output: apples

def remove_numbers(input_str):
    output = ''.join([char for char in input_str if not char.isdigit()])
    return output

# Test cases
print(remove_numbers('apples30'))  # Output: apples
print(remove_numbers('peaches24'))  # Output: peaches
print(remove_numbers('peaches0'))   # Output: peaches
print(remove_numbers('pears'))      # Output: pears
