# Prompt: return everything after the last "/" in input
# Input: 'c=/users/dave/shotcut.xls'
# Output: shotcut.xls

def get_last_part(input_str):
    return input_str.split('/')[-1]

# Test cases
print(get_last_part('c=/users/dave/shotcut.xls'))  # Output: shotcut.xls
print(get_last_part('c=/users/dave/formulas.xls'))  # Output: formulas.xls
print(get_last_part('c=/users/dave/pivot table.xls'))  # Output: pivot table.xls
