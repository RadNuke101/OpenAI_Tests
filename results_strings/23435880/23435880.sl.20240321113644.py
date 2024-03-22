# Prompt: return the number of the times the entered word (second column) appears in the expression (first column)
# Input: ['apple apples', 'apple']
# Output: 2

def count_word_appearances(expression, word):
    return str(expression.count(word))

# Test the function with the provided inputs
input1 = 'apple apples'
input2 = 'apple'
output = count_word_appearances(input1, input2)
print(output)  # Output should be 2
