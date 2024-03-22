# Prompt: returns letter at entered position (second column) in expression (first column)
# Input: 'spreadsheet', '1'
# Output: s

def get_letter(expression, position):
    return expression[int(position) - 1]

# Test cases
print(get_letter('spreadsheet', '1'))  # Output: s
print(get_letter('spreadsheet', '2'))  # Output: p
print(get_letter('spreadsheet', '3'))  # Output: r
print(get_letter('spreadsheet', '4'))  # Output: e
print(get_letter('spreadsheet', '5'))  # Output: a
