# Prompt: return everything after the last "/" in input
# Input: 'home/Excel/Sheet1.xls'
# Output: 'Sheet1.xls'

def get_last_part(input_str):
    parts = input_str.split('/')
    return parts[-1]

# Test the function with the provided inputs
print(get_last_part('home/Excel/Sheet1.xls'))  # Output: 'Sheet1.xls'
print(get_last_part('home/user/Sheet1.xls'))  # Output: 'Sheet1.xls'
