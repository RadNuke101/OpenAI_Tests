# Prompt: returns letter at entered position (second column) in expression (first column)
# Input: ['spreadsheet', '1'] 
# Output: s
# Input: ['spreadsheet', '2'] 
# Output: p
# Input: ['spreadsheet', '3'] 
# Output: r
# Input: ['spreadsheet', '4'] 
# Output: e
# Input: ['spreadsheet', '5'] 
# Output: a

def get_letter_at_position(expression, position):
    return expression[int(position) - 1]

# Test cases
print(get_letter_at_position('spreadsheet', '1'))  # Output: s
print(get_letter_at_position('spreadsheet', '2'))  # Output: p
print(get_letter_at_position('spreadsheet', '3'))  # Output: r
print(get_letter_at_position('spreadsheet', '4'))  # Output: e
print(get_letter_at_position('spreadsheet', '5'))  # Output: a
