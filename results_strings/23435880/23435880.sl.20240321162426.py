# Prompt: return the number of times the entered word (second column) appears in the expression (first column)
# Input: ['apple apples', 'apple']
# Output: 2

def count_word_appearances(input_str, word):
    count = input_str.count(word)
    return count

# Test the function with the provided inputs
input_str = 'apple apples'
word = 'apple'
output = count_word_appearances(input_str, word)
print(output)  # Output should be 2
