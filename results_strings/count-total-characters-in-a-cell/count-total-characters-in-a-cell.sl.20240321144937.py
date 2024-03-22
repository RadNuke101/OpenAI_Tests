# Prompt: return the number of characters in the inputted expression
# Input: 'The'  Output: 3
# Input: 'The quick fox'  Output: 13
# Input: 'The quick  fox'  Output: 14

def count_characters(input_str):
    return len(input_str)

# Test cases
print(count_characters('The'))  # Output: 3
print(count_characters('The quick fox'))  # Output: 13
print(count_characters('The quick  fox'))  # Output: 14
