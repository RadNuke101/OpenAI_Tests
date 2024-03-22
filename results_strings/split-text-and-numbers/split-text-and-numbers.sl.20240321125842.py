# Prompt: remove numbers from first input
# Input: ['apples30', '7'] 
# Output: apples

def remove_numbers(input):
    first_input = input.split(',')[0]
    output = ''.join([i for i in first_input if not i.isdigit()])
    return output

# Test cases
print(remove_numbers('apples30,7'))  # Output: apples
print(remove_numbers('peaches24,8'))  # Output: peaches
print(remove_numbers('peaches0,8'))   # Output: peaches
print(remove_numbers('pears,6'))      # Output: pears
