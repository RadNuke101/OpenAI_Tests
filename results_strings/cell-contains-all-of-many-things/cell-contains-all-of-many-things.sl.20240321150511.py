# Prompt: if the second, third, and fourth inputs (words) are in the first input (expression), then return true, else false
# Input: ['yellow dog on green grass', 'yellow', 'green', 'dog'] 
# Output: true
# Input: ['Lone dog with a green frisbie on yellow sand', 'yellow', 'green', 'dog'] 
# Output: true
# Input: ['A yellow sun in a green field', 'yellow', 'green', 'dog'] 
# Output: false
# Input: ['yellow neon sign with a green background', 'yellow', 'green', 'dog'] 
# Output: false

def check_words_in_expression(expression, word1, word2, word3):
    words = expression.split()
    return word1 in words and word2 in words and word3 in words

# Test cases
print(check_words_in_expression('yellow dog on green grass', 'yellow', 'green', 'dog'))  # Output: true
print(check_words_in_expression('Lone dog with a green frisbie on yellow sand', 'yellow', 'green', 'dog'))  # Output: true
print(check_words_in_expression('A yellow sun in a green field', 'yellow', 'green', 'dog'))  # Output: false
print(check_words_in_expression('yellow neon sign with a green background', 'yellow', 'green', 'dog'))  # Output: false
