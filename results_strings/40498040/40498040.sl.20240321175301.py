# Prompt: if the word "overhead" is in expression, return false, else true
# Input: ['some project,other project'] Output: true
# Input: ['some project'] Output: true
# Input: ['overhead'] Output: false
# Input: ['some project, overhead'] Output: false
# Input: ['some project, other, boo'] Output: true

def check_overhead(input_str):
    if 'overhead' in input_str:
        return 'false'
    else:
        return 'true'

# Test cases
print(check_overhead('some project,other project'))  # Output: true
print(check_overhead('some project'))  # Output: true
print(check_overhead('overhead'))  # Output: false
print(check_overhead('some project, overhead'))  # Output: false
print(check_overhead('some project, other, boo'))  # Output: true
