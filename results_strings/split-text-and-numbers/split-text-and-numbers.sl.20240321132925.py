# Prompt: remove numbers from first input
# Input: ['apples30', '7'] 
# Output: apples

def remove_numbers(input):
    word = input.split()[0]
    result = ''.join([i for i in word if not i.isdigit()])
    return result

# Test cases
print(remove_numbers('apples30 7'))  # Output: apples
print(remove_numbers('peaches24 8'))  # Output: peaches
print(remove_numbers('peaches0 8'))   # Output: peaches
print(remove_numbers('pears 6'))      # Output: pears
