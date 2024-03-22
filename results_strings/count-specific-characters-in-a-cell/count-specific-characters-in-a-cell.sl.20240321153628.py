# Prompt: return the number of times the second input (case-sensitive letter) appears in the inputted expression (first input)
# Input: ['Hannah', 'n'] Output: 2
# Input: ['Hannah', 'x'] Output: 0
# Input: ['Hannah', 'N'] Output: 0
# Input: ['Hannah', 'a'] Output: 2
# Input: ['Hannah', 'h'] Output: 1

def count_letter_occurrences(input_str, letter):
    return input_str.count(letter)

# Test cases
print(count_letter_occurrences('Hannah', 'n'))  # Output: 2
print(count_letter_occurrences('Hannah', 'x'))  # Output: 0
print(count_letter_occurrences('Hannah', 'N'))  # Output: 0
print(count_letter_occurrences('Hannah', 'a'))  # Output: 2
print(count_letter_occurrences('Hannah', 'h'))  # Output: 1
