# Prompt: if entered letter or phrase (second column) is in the expression (first column), return true, else false
# Input: ['ABC', 'D'] 
# Output: false
# Input: ['ABC', 'BC'] 
# Output: true

def check_input(expression, check):
    return str(check) in str(expression)

# Test cases
print(check_input('ABC', 'D'))  # Output: false
print(check_input('ABC', 'BC'))  # Output: true
