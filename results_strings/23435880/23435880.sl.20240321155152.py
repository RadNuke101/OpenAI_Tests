# Prompt: return the number of times the entered word (second column) appears in the expression (first column)
# Input: 'apple apples', 'apple'
# Output: 2

def count_word_appearances(expression, word):
    return str(expression.count(word))

# Test the function with the provided inputs
input_str = 'apple apples', 'apple'
output_str = count_word_appearances(input_str[0], input_str[1])
print(output_str)
