# Prompt: remove numbers from first input
# Input: ['apples30', '7'] -> Output: 'apples'
# Input: ['peaches24', '8'] -> Output: 'peaches'
# Input: ['peaches0', '8'] -> Output: 'peaches'
# Input: ['pears', '6'] -> Output: 'pears'

def remove_numbers(input):
    first_input = input[0]
    output = ''.join([char for char in first_input if not char.isdigit()])
    return output

# Test cases
print(remove_numbers(['apples30', '7']))  # Output: 'apples'
print(remove_numbers(['peaches24', '8']))  # Output: 'peaches'
print(remove_numbers(['peaches0', '8']))  # Output: 'peaches'
print(remove_numbers(['pears', '6']))  # Output: 'pears'
