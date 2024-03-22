# Prompt: return everything after the last "/" in input
# Input: 'home/Excel/Sheet1.xls'
# Output: 'Sheet1.xls'

def get_last_segment(input_str):
    segments = input_str.split('/')
    return segments[-1]

# Test cases
input1 = 'home/Excel/Sheet1.xls'
output1 = get_last_segment(input1)
print(output1)  # Output: 'Sheet1.xls'

input2 = 'home/user/Sheet1.xls'
output2 = get_last_segment(input2)
print(output2)  # Output: 'Sheet1.xls'
