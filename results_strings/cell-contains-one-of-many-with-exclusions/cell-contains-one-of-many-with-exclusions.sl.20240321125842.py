def check_inputs(input_str, first_word, second_word, third_word):
    words = input_str.split()
    if first_word in words[0] or first_word in words[1]:
        return True
    elif second_word in words[0] or second_word in words[1]:
        return True
    elif third_word in words[0] or third_word in words[1]:
        return True
    else:
        return False

# Prompt: if only one of the inputs from the second, third, or fourth column are in the first two words of the first input, return true, else false
# Input: ['yellow dog on green grass', 'yellow', 'green', 'cat'] Output: true
# Input: ['warm gray sweater', 'yellow', 'green', 'cat'] Output: false
# Input: ['blue neon signs', 'blue', 'green', 'neon'] Output: false
# Input: ['hot pink socks', 'blue', 'pink', 'neon'] Output: true
# Input: ['deep black eyes', 'yellow', 'green', 'neon'] Output: false

# Test cases
print(check_inputs('yellow dog on green grass', 'yellow', 'green', 'cat'))  # Output: true
print(check_inputs('warm gray sweater', 'yellow', 'green', 'cat'))  # Output: false
print(check_inputs('blue neon signs', 'blue', 'green', 'neon'))  # Output: false
print(check_inputs('hot pink socks', 'blue', 'pink', 'neon'))  # Output: true
print(check_inputs('deep black eyes', 'yellow', 'green', 'neon'))  # Output: false
