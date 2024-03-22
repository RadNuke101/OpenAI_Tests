def check_input_output(input_str):
    inputs = input_str.split(', ')
    expression = inputs[0]
    words = inputs[1:]

    for word in words:
        if word in expression:
            return 'true'
    
    return 'false'

# Prompt: if either the second, third, or fourth inputs (words) are in the first input (expression), return true, else false
# Input: ['yellow dog on green grass', 'yellow', 'green', 'dog']
# Output: true
# Input: ['warm gray sweater', 'yellow', 'green', 'dog']
# Output: false
# Input: ['A yellow sun in a green field', 'yellow', 'green', 'dog']
# Output: true
# Input: ['yellow neon sign with a green background', 'yellow', 'green', 'dog']
# Output: true
