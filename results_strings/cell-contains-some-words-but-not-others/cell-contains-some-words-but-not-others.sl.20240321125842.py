# Prompt: if the second input (word) is in the first input (expression), return true, else false
# Input: 'red ball, green sweater', 'red', 'green', 'pink'
# Output: true

def check_word_in_expression(expression, *words):
    for word in words:
        if word in expression:
            return "true"
    return "false"

# Test cases
print(check_word_in_expression('red ball, green sweater', 'red', 'green', 'pink'))  # Output: true
print(check_word_in_expression('pink ball, green sweater', 'red', 'green', 'pink'))  # Output: false
print(check_word_in_expression('blue sea, pink ribbon', 'red', 'blue', 'pink'))  # Output: false
print(check_word_in_expression('black sea, white ribbon', 'red', 'blue', 'pink'))  # Output: false
print(check_word_in_expression('red green blue', 'red', 'blue', 'pink'))  # Output: true
