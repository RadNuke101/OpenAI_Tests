# Prompt: if only one of the inputs from the second, third, or fourth column are in the first two words of the first input, return true, else false
# Input: ['yellow dog on green grass', 'yellow', 'green', 'cat']
# Output: true

def check_inputs(input_str, input1, input2, input3):
    first_two_words = input_str.split()[:2]
    count = 0
    if input1 in first_two_words:
        count += 1
    if input2 in first_two_words:
        count += 1
    if input3 in first_two_words:
        count += 1
    
    return count == 1

# Test cases
print(check_inputs('yellow dog on green grass', 'yellow', 'green', 'cat'))  # Output: true
print(check_inputs('warm gray sweater', 'yellow', 'green', 'cat'))  # Output: false
print(check_inputs('blue neon signs', 'blue', 'green', 'neon'))  # Output: false
print(check_inputs('hot pink socks', 'blue', 'pink', 'neon'))  # Output: true
print(check_inputs('deep black eyes', 'yellow', 'green', 'neon'))  # Output: false
