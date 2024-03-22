# Prompt: return first three numbers in input
# Input: ['+106 769-858-438'], Output: 106
# Input: ['+83 973-757-831'], Output: 83
# Input: ['+62 647-787-775'], Output: 62
# Input: ['+172 027-507-632'], Output: 172
# Input: ['+72 001-050-856'], Output: 72
# Input: ['+95 310-537-401'], Output: 95
# Input: ['+6 775-969-238'], Output: 6

def extract_first_three_numbers(input_str):
    return input_str.split()[0][1:]

# Test the function with one of the inputs
input_str = '+106 769-858-438'
output_str = extract_first_three_numbers(input_str)
print(output_str)  # Output: 106
