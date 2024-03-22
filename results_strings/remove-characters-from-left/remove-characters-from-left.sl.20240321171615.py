# Prompt: From the left, delete the number (second input) of elements from the first input
# Input: ['1234', '1'] 
# Output: 234
# Input: ['**512A', '2'] 
# Output: 512A
# Input: ['343DMX', '3'] 
# Output: DMX

def delete_elements(input_str, num_elements):
    return input_str[int(num_elements):]

# Test cases
print(delete_elements('1234', '1'))  # Output: 234
print(delete_elements('**512A', '2'))  # Output: 512A
print(delete_elements('343DMX', '3'))  # Output: DMX
