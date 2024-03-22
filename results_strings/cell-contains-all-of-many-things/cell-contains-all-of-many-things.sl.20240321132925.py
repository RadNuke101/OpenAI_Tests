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
    words = [word1, word2, word3]
    for word in words:
        if word not in expression:
            return False
    return True

# Test cases
print(check_words_in_expression('yellow dog on green grass', 'yellow', 'green', 'dog'))  # Output: true
print(check_words_in_expression('Lone dog with a green frisbie on yellow sand', 'yellow', 'green', 'dog'))  # Output: true
print(check_words_in_expression('A yellow sun in a green field', 'yellow', 'green', 'dog'))  # Output: false
print(check_words_in_expression('yellow neon sign with a green background', 'yellow', 'green', 'dog'))  # Output: false
