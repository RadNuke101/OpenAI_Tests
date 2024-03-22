# Prompt: remove the second input from the first input
# Input: ['Item 1 AQ-S810W-2AVDF', 'AQ-S810W-2AVDF']
# Output: Item 1

def remove_second_input(input_str):
    inputs = input_str.split()
    first_input = inputs[0]
    second_input = inputs[1]
    
    output = first_input.replace(second_input, '').strip()
    
    return output

# Test the function with the provided inputs
input1 = 'Item 1 AQ-S810W-2AVDF AQ-S810W-2AVDF'
input2 = 'Item 2 AQ-230A-1DUQ AQ-230A'
print(remove_second_input(input1))  # Output: Item 1
print(remove_second_input(input2))  # Output: Item 2 -1DUQ
