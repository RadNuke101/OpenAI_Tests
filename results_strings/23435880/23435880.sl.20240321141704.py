# Prompt: return the number of the times the entered word (second column) appears in the expression (first column)
# Input: 'apple apples', 'apple'
# Output: 2
# Input: 'an orange among the oranges is a spoiled orange', 'orange'
# Output: 3

def count_word_appearances(expression, word):
    return str(expression.count(word))

# Test cases
print(count_word_appearances('apple apples', 'apple'))  # Output: 2
print(count_word_appearances('an orange among the oranges is a spoiled orange', 'orange'))  # Output: 3
