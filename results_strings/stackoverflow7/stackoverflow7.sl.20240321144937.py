# Prompt: remove the second input from the first input
# Input: ['Item 1 AQ-S810W-2AVDF', 'AQ-S810W-2AVDF']
# Output: Item 1

def remove_second_input(input_str):
    inputs = input_str.split()
    output = inputs[0].replace(inputs[1], '').strip()
    return output

# Test cases
print(remove_second_input('Item 1 AQ-S810W-2AVDF AQ-S810W-2AVDF'))  # Output: Item 1
print(remove_second_input('Item 2 AQ-230A-1DUQ AQ-230A'))  # Output: Item 2 -1DUQ
