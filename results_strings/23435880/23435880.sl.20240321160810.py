# Prompt: return the number of times the entered word (second column) appears in the expression (first column)
# Input: ['apple apples', 'apple']
# Output: 2

def count_word_appearances(expression, word):
    return str(expression.count(word))

# Test the function with the given input
input_str = 'apple apples'
word_to_count = 'apple'
output_str = count_word_appearances(input_str, word_to_count)
print(output_str)
