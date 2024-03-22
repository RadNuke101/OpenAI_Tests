# Prompt: return the number of times the second input (case-sensitive phrase) appears in the first input (expression)
# Input: 'The fox jumped over the fox', 'fox'
# Output: 2

def count_occurrences(expression, phrase):
    return expression.count(phrase)

# Test the function with the provided inputs
input1 = 'The fox jumped over the fox'
input2 = 'fox'
output = count_occurrences(input1, input2)
print(output)  # Output: 2
