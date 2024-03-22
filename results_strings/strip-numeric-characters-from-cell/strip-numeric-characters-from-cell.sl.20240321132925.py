# Prompt: remove the numbers from input
# Given input as '34653 jim mcdonald' output is 'jim mcdonald'
# Given input as 'price is 500' output is 'price is'
# Given input as '100 apples' output is 'apples'

def remove_numbers(input_str):
    output = ''.join([char for char in input_str if not char.isdigit()])
    return output.strip()

# Test cases
print(remove_numbers('34653 jim mcdonald'))  # Output: 'jim mcdonald'
print(remove_numbers('price is 500'))  # Output: 'price is'
print(remove_numbers('100 apples'))  # Output: 'apples'
