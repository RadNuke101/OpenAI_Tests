# Prompt: remove the second input from the first input

def remove_second_input(input1, input2):
    output = input1.replace(input2, '').strip()
    return output

# Input: ['Item 1 AQ-S810W-2AVDF', 'AQ-S810W-2AVDF']
# Output: Item 1
print(remove_second_input('Item 1 AQ-S810W-2AVDF', 'AQ-S810W-2AVDF'))

# Input: ['Item 2 AQ-230A-1DUQ', 'AQ-230A']
# Output: Item 2 -1DUQ
print(remove_second_input('Item 2 AQ-230A-1DUQ', 'AQ-230A'))
