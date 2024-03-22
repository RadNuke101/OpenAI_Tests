def check_inputs(input_str, first_word, second_word, third_word):
    words = input_str.split()
    first_two_words = ' '.join(words[:2])
    
    if first_word in first_two_words or second_word in first_two_words or third_word in first_two_words:
        return 'true'
    else:
        return 'false'

# Prompt: if only one of the inputs from the second, third, or fourth column are in the first two words of the first input (first column), return true, else false
# Input: ['yellow dog on green grass', 'yellow', 'green', 'cat']
# Output: true
# Input: ['warm gray sweater', 'yellow', 'green', 'cat']
# Output: false
# Input: ['blue neon signs', 'blue', 'green', 'neon']
# Output: false
# Input: ['hot pink socks', 'blue', 'pink', 'neon']
# Output: true
# Input: ['deep black eyes', 'yellow', 'green', 'neon']
# Output: false
