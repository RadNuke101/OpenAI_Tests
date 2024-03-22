# Prompt: return last three numbers in input
# Input: ['+106 769-858-438'], Output: 438
# Input: ['+83 973-757-831'], Output: 831
# Input: ['+62 647-787-775'], Output: 775
# Input: ['+172 027-507-632'], Output: 632
# Input: ['+72 001-050-856'], Output: 856
# Input: ['+95 310-537-401'], Output: 401
# Input: ['+6 775-969-238'], Output: 238

def get_last_three_numbers(input_str):
    return input_str[-3:]

# Test the function with an example input
input_example = '+106 769-858-438'
output_example = get_last_three_numbers(input_example)
print(output_example)  # Output: 438
