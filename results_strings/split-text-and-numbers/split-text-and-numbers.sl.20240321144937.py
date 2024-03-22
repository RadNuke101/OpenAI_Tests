# Prompt: remove numbers from first input
# Given input as ['apples30', '7'] output is apples
# Given input as ['peaches24', '8'] output is peaches
# Given input as ['peaches0', '8'] output is peaches
# Given input as ['pears', '6'] output is pears

def remove_numbers(input_str):
    output = ''.join([char for char in input_str if not char.isdigit()])
    return output

# Test cases
print(remove_numbers('apples30'))  # Output: apples
print(remove_numbers('peaches24'))  # Output: peaches
print(remove_numbers('peaches0'))   # Output: peaches
print(remove_numbers('pears'))      # Output: pears
