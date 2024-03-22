# Prompt: return the number of times the entered word (second column) appears in the expression (first column)
# Input: ['apple apples', 'apple']
# Output: 2

def count_word_appearances(expression, word):
    return str(expression.count(word))

# Test the function with the provided inputs
input_1 = 'apple apples', 'apple'
output_1 = count_word_appearances(input_1[0], input_1[1])
print(output_1)

# Input: ['an orange among the oranges is a spoiled orange', 'orange']
# Output: 3

input_2 = 'an orange among the oranges is a spoiled orange', 'orange'
output_2 = count_word_appearances(input_2[0], input_2[1])
print(output_2)
