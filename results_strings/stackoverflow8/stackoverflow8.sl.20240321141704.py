# Prompt: return everything after the last "/" in input
# Input: 'home/Excel/Sheet1.xls'
# Output: 'Sheet1.xls'

def get_last_segment(input_str):
    segments = input_str.split('/')
    return segments[-1]

# Test the function with the provided inputs
print(get_last_segment('home/Excel/Sheet1.xls'))  # Output: 'Sheet1.xls'
print(get_last_segment('home/user/Sheet1.xls'))   # Output: 'Sheet1.xls'
