# Prompt: return the number of times the entered word (second column) appears in the expression (first column)
# Input: ['apple apples', 'apple']
# Output: 2

def count_word_appearances(expression, word):
    count = expression.count(word)
    return count

# Test the function with the given inputs
input1 = 'apple apples'
input2 = 'apple'
output = count_word_appearances(input1, input2)
print(output)  # Output: 2
