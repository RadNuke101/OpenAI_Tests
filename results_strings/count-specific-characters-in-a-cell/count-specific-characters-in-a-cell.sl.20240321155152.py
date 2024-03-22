# Prompt: return the number of times the second input (case-sensitive letter) appears in the inputted expression (first input)
# Input: ['Hannah', 'n'] 
# Output: 2
def count_letter_appearances(expression, letter):
    return str(expression.count(letter))

# Test cases
print(count_letter_appearances('Hannah', 'n'))  # Output: 2
print(count_letter_appearances('Hannah', 'x'))  # Output: 0
print(count_letter_appearances('Hannah', 'N'))  # Output: 0
print(count_letter_appearances('Hannah', 'a'))  # Output: 2
print(count_letter_appearances('Hannah', 'h'))  # Output: 1
