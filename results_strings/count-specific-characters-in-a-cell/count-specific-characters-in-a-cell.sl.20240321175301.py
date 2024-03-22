# Prompt: return the number of times the second input (case-sensitive letter) appears in the inputted expression (first input)
# Input: ['Hannah', 'n'] Output: 2
# Input: ['Hannah', 'x'] Output: 0
# Input: ['Hannah', 'N'] Output: 0
# Input: ['Hannah', 'a'] Output: 2
# Input: ['Hannah', 'h'] Output: 1

def count_letter_appearance(expression, letter):
    return str(expression).count(letter)

# Test cases
print(count_letter_appearance('Hannah', 'n'))  # Output: 2
print(count_letter_appearance('Hannah', 'x'))  # Output: 0
print(count_letter_appearance('Hannah', 'N'))  # Output: 0
print(count_letter_appearance('Hannah', 'a'))  # Output: 2
print(count_letter_appearance('Hannah', 'h'))  # Output: 1
