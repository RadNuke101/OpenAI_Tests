def check_input_output(expression, *words):
    for word in words:
        if word in expression:
            return "true"
    return "false"

# Prompt: if the second input (word) is in the first input (expression), return true, else false
# Input: 'red ball, green sweater', 'red', 'green', 'pink'
# Output: true
# Input: 'pink ball, green sweater', 'red', 'green', 'pink'
# Output: false
# Input: 'blue sea, pink ribbon', 'red', 'blue', 'pink'
# Output: false
# Input: 'black sea, white ribbon', 'red', 'blue', 'pink'
# Output: false
# Input: 'red green blue', 'red', 'blue', 'pink'
# Output: true
