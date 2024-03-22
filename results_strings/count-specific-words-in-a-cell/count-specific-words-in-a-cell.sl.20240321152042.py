# Prompt: return the number of times the second input (case-sensitive phrase) appears in the first input (expression)
# Input: 'The fox jumped over the fox', 'fox'
# Output: 2

def count_appearance(expression, phrase):
    return expression.count(phrase)

# Test cases
print(count_appearance('The fox jumped over the fox', 'fox'))  # Output: 2
print(count_appearance('The fox jumped over the fox', 'ox'))   # Output: 2
print(count_appearance('The fox jumped over the fox', 'Fox'))   # Output: 0
2
2
0
