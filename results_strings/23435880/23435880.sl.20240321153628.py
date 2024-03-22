# Prompt: return the number of times the entered word (second column) appears in the expression (first column)
# Input: 'apple apples', 'apple'
# Output: 2
# Input: 'an orange among the oranges is a spoiled orange', 'orange'
# Output: 3

def count_word_appearance(expression, word):
    return str(expression.count(word))

# Test the function with the provided inputs
input1 = 'apple apples', 'apple'
output1 = count_word_appearance(input1[0], input1[1])
print(output1)  # Output: 2

input2 = 'an orange among the oranges is a spoiled orange', 'orange'
output2 = count_word_appearance(input2[0], input2[1])
print(output2)  # Output: 3
