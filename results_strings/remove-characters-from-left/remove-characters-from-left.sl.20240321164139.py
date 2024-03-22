def delete_elements(input_str, num_elements):
    return input_str[num_elements:]

# Prompt input and output examples:
# Input: ['1234', '1'], Output: 234
# Input: ['**512A', '2'], Output: 512A
# Input: ['343DMX', '3'], Output: DMX

# Test the function with the provided examples
print(delete_elements('1234', 1))  # Output: 234
print(delete_elements('**512A', 2))  # Output: 512A
print(delete_elements('343DMX', 3))  # Output: DMX
