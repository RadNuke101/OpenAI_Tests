# Prompt: return everything after the last "/" in input
# Input: ['home/Excel/Sheet1.xls']
# Output: Sheet1.xls

def get_last_part(input_str):
    parts = input_str.split('/')
    return parts[-1]

# Test the function with the provided inputs
input_str1 = 'home/Excel/Sheet1.xls'
output_str1 = get_last_part(input_str1)
print(output_str1)  # Output: Sheet1.xls

input_str2 = 'home/user/Sheet1.xls'
output_str2 = get_last_part(input_str2)
print(output_str2)  # Output: Sheet1.xls
