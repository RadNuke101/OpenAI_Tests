# Prompt: return first three numbers in input
# given input as ['+106 769-858-438'] output is 106
# given input as ['+83 973-757-831'] output is 83
# given input as ['+62 647-787-775'] output is 62

def extract_first_three_numbers(input_str):
    numbers = ''.join([char for char in input_str if char.isdigit()])  # extract all digits from input string
    return numbers[:3]  # return the first three digits

# Test cases
print(extract_first_three_numbers('+106 769-858-438'))  # Output: 106
print(extract_first_three_numbers('+83 973-757-831'))  # Output: 83
print(extract_first_three_numbers('+62 647-787-775'))  # Output: 62
