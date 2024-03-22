def check_expression(input_str):
    input_list = input_str.split(', ')
    expression = input_list[0]
    words = input_list[1:]

    for word in words:
        if word not in expression:
            return 'false'
    
    return 'true'

# Prompt: if the second, third, and fourth inputs (words) are in the first input (expression), then return true, else false
# Input: ['yellow dog on green grass', 'yellow', 'green', 'dog']
# Output: true
# Input: ['Lone dog with a green frisbie on yellow sand', 'yellow', 'green', 'dog']
# Output: true
# Input: ['A yellow sun in a green field', 'yellow', 'green', 'dog']
# Output: false
# Input: ['yellow neon sign with a green background', 'yellow', 'green', 'dog']
# Output: false
