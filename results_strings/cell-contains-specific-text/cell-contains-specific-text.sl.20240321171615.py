# Prompt: if the second input (word or phrase) is in the first input (expression), return true, else false
# Input: 'An apple a day keeps the doctor away', 'apple'
# Output: true
# Input: 'An apple a day keeps the doctor away', 'orange'
# Output: false
# Input: 'Better the devil you know', 'you know'
# Output: true

def check_input_in_expression(expression, word):
    return str(word in expression)

# Test cases
print(check_input_in_expression('An apple a day keeps the doctor away', 'apple'))  # Output: true
print(check_input_in_expression('An apple a day keeps the doctor away', 'orange'))  # Output: false
print(check_input_in_expression('Better the devil you know', 'you know'))  # Output: true
