# Start time: 2024-03-30 03:04:29.321910
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: if the second input (word) is in the first input (expresssion), return true, else false, and given input as ['red ball, green sweater', 'red', 'green', 'pink'] output is true, given input as ['pink ball, green sweater', 'red', 'green', 'pink'] output is false, given input as ['blue sea, pink ribbon', 'red', 'blue', 'pink'] output is false, given input as ['black sea, white ribbon', 'red', 'blue', 'pink'] output is false, given input as ['red green blue', 'red', 'blue', 'pink'] output is true, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
def check_input_output(expression, word1, word2, word3):
    try:
        if word1 in expression and word2 in expression:
            return "true"
        else:
            return "false"
    except Exception as e:
        return str(e)

# Input: 'red ball, green sweater', 'red', 'green', 'pink'
# Output: true
print(check_input_output('red ball, green sweater', 'red', 'green', 'pink'))

# Input: 'pink ball, green sweater', 'red', 'green', 'pink'
# Output: false
print(check_input_output('pink ball, green sweater', 'red', 'green', 'pink'))

# Input: 'blue sea, pink ribbon', 'red', 'blue', 'pink'
# Output: false
print(check_input_output('blue sea, pink ribbon', 'red', 'blue', 'pink'))

# Input: 'black sea, white ribbon', 'red', 'blue', 'pink'
# Output: false
print(check_input_output('black sea, white ribbon', 'red', 'blue', 'pink'))

# Input: 'red green blue', 'red', 'blue', 'pink'
# Output: true
print(check_input_output('red green blue', 'red', 'blue', 'pink'))

# End time: 2024-03-30 03:04:35.368237
# Elapsed time in seconds: 6.046163149998392