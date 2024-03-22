# Prompt: if only one of the inputs from the second, third, or fourth column are in the first two words of the first input, return true, else false
# Input: ['yellow dog on green grass', 'yellow', 'green', 'cat']
# Output: true

def check_inputs(input_str, word1, word2, word3):
    words = input_str.split()
    first_two_words = ' '.join(words[:2])
    
    count = 0
    if word1 in first_two_words:
        count += 1
    if word2 in first_two_words:
        count += 1
    if word3 in first_two_words:
        count += 1
    
    return count == 1

# Test cases
print(check_inputs('yellow dog on green grass', 'yellow', 'green', 'cat'))  # Output: True
print(check_inputs('warm gray sweater', 'yellow', 'green', 'cat'))  # Output: False
print(check_inputs('blue neon signs', 'blue', 'green', 'neon'))  # Output: False
print(check_inputs('hot pink socks', 'blue', 'pink', 'neon'))  # Output: True
print(check_inputs('deep black eyes', 'yellow', 'green', 'neon'))  # Output: False
