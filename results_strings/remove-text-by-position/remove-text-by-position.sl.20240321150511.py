# Prompt: return everything after the last "/" in input
# Input: 'c=/users/dave/shotcut.xls'
# Output: shotcut.xls

def get_last_segment(input_str):
    segments = input_str.split('/')
    return segments[-1]

# Test cases
print(get_last_segment('c=/users/dave/shotcut.xls'))  # Output: shotcut.xls
print(get_last_segment('c=/users/dave/formulas.xls'))  # Output: formulas.xls
print(get_last_segment('c=/users/dave/pivot table.xls'))  # Output: pivot table.xls
