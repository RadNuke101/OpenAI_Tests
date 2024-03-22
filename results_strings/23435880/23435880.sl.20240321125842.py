# Prompt: return the number of times the entered word (second column) appears in the expression (first column)
# Input: ['apple apples', 'apple']
# Output: 2

def count_word_appearances(expression, word):
    return str(expression.count(word))

# Test the function with the given inputs
input_1 = 'apple apples'
input_2 = 'apple'
output = count_word_appearances(input_1, input_2)
print(output)  # Output should be 2
