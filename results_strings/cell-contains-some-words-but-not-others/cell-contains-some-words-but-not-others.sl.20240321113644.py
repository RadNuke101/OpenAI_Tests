# Prompt: if the second input (word) is in the first input (expression), return true, else false
# Input: ['red ball, green sweater', 'red', 'green', 'pink'] Output: true
# Input: ['pink ball, green sweater', 'red', 'green', 'pink'] Output: false
# Input: ['blue sea, pink ribbon', 'red', 'blue', 'pink'] Output: false
# Input: ['black sea, white ribbon', 'red', 'blue', 'pink'] Output: false
# Input: ['red green blue', 'red', 'blue', 'pink'] Output: true

def check_word_in_expression(expression, word1, word2, word3):
    if word1 in expression and (word2 in expression or word3 in expression):
        return "true"
    else:
        return "false"

# Test cases
print(check_word_in_expression('red ball, green sweater', 'red', 'green', 'pink'))  # Output: true
print(check_word_in_expression('pink ball, green sweater', 'red', 'green', 'pink'))  # Output: false
print(check_word_in_expression('blue sea, pink ribbon', 'red', 'blue', 'pink'))  # Output: false
print(check_word_in_expression('black sea, white ribbon', 'red', 'blue', 'pink'))  # Output: false
print(check_word_in_expression('red green blue', 'red', 'blue', 'pink'))  # Output: true
