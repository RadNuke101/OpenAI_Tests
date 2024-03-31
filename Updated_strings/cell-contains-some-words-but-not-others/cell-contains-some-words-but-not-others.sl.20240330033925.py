# Start time: 2024-03-30 03:40:28.345656
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: if the second input (word) is in the first input (expresssion), return true, else false, and given input as ['red ball, green sweater', 'red', 'green', 'pink'] output is true, given input as ['pink ball, green sweater', 'red', 'green', 'pink'] output is false, given input as ['blue sea, pink ribbon', 'red', 'blue', 'pink'] output is false, given input as ['black sea, white ribbon', 'red', 'blue', 'pink'] output is false, given input as ['red green blue', 'red', 'blue', 'pink'] output is true, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
def check_input_output(expression, *words):
    try:
        expression = expression.split(', ')
        for word in words:
            if word in expression:
                return True
        return False
    except Exception as e:
        return f"Error: {e}"

# Input: 'red ball, green sweater', 'red', 'green', 'pink'
# Output: True
# Prompt: if the second input (word) is in the first input (expression), return true, else false

# Input: 'pink ball, green sweater', 'red', 'green', 'pink'
# Output: False

# Input: 'blue sea, pink ribbon', 'red', 'blue', 'pink'
# Output: False

# Input: 'black sea, white ribbon', 'red', 'blue', 'pink'
# Output: False

# Input: 'red green blue', 'red', 'blue', 'pink'
# Output: True

# End time: 2024-03-30 03:40:30.480596
# Elapsed time in seconds: 2.1348406160013838