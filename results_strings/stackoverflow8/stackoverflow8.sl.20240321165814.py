# Prompt: return everything after the last "/" in input
# Input: ['home/Excel/Sheet1.xls']
# Output: Sheet1.xls

def get_last_part(input_str):
    return input_str.rsplit('/', 1)[-1]

# Test the function with the provided inputs
input_1 = 'home/Excel/Sheet1.xls'
output_1 = get_last_part(input_1)
print(output_1)  # Output: Sheet1.xls

input_2 = 'home/user/Sheet1.xls'
output_2 = get_last_part(input_2)
print(output_2)  # Output: Sheet1.xls
