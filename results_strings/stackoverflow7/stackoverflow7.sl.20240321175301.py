# Prompt: remove the second input from the first input
# Input: ['Item 1 AQ-S810W-2AVDF', 'AQ-S810W-2AVDF']
# Output: Item 1
def remove_second_input(input):
    first_input = input.split()[0]
    second_input = input.split()[1]
    output = first_input.replace(second_input, '').strip()
    return output

# Test cases
print(remove_second_input('Item 1 AQ-S810W-2AVDF AQ-S810W-2AVDF'))  # Output: Item 1
print(remove_second_input('Item 2 AQ-230A-1DUQ AQ-230A'))  # Output: Item 2 -1DUQ
