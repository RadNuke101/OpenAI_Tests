# Prompt: if the second input (word) is in the first input (expression), return true, else false
# Input: ['red ball, green sweater', 'red', 'green', 'pink'] 
# Output: true

def check_word_in_expression(expression, word):
    return word in expression

# Test cases
print(check_word_in_expression('red ball, green sweater', 'red')) # Output: True
print(check_word_in_expression('red ball, green sweater', 'green')) # Output: True
print(check_word_in_expression('red ball, green sweater', 'pink')) # Output: False
print(check_word_in_expression('pink ball, green sweater', 'red')) # Output: False
print(check_word_in_expression('blue sea, pink ribbon', 'red')) # Output: False
print(check_word_in_expression('blue sea, pink ribbon', 'blue')) # Output: True
print(check_word_in_expression('red green blue', 'red')) # Output: True
print(check_word_in_expression('red green blue', 'pink')) # Output: False
