# Prompt: remove the numbers from input
# Input: '34653 jim mcdonald'
# Output: 'jim mcdonald'

def remove_numbers(input_str):
    output_str = ''.join([char for char in input_str if not char.isdigit()])
    return output_str

# Test cases
print(remove_numbers('34653 jim mcdonald'))  # Output: 'jim mcdonald'
print(remove_numbers('price is 500'))  # Output: 'price is '
print(remove_numbers('100 apples'))  # Output: 'apples'
