# Start time: 2024-03-30 05:07:16.745683
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: if the second input (word) is in the first input (expresssion), return true, else false, and given input as ['red ball, green sweater', 'red', 'green', 'pink'] output is true, given input as ['pink ball, green sweater', 'red', 'green', 'pink'] output is false, given input as ['blue sea, pink ribbon', 'red', 'blue', 'pink'] output is false, given input as ['black sea, white ribbon', 'red', 'blue', 'pink'] output is false, given input as ['red green blue', 'red', 'blue', 'pink'] output is true, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
def check_input_output(expression, *words):
    try:
        for word in words:
            if word in expression:
                return True
        return False
    except Exception as e:
        print("An error occurred:", e)

# Input: 'red ball, green sweater', 'red', 'green', 'pink'
# Output: True
# Prompt: if the second input (word) is in the first input (expression), return true, else false
print(check_input_output('red ball, green sweater', 'red', 'green', 'pink'))

# Input: 'pink ball, green sweater', 'red', 'green', 'pink'
# Output: False
print(check_input_output('pink ball, green sweater', 'red', 'green', 'pink'))

# Input: 'blue sea, pink ribbon', 'red', 'blue', 'pink'
# Output: False
print(check_input_output('blue sea, pink ribbon', 'red', 'blue', 'pink'))

# Input: 'black sea, white ribbon', 'red', 'blue', 'pink'
# Output: False
print(check_input_output('black sea, white ribbon', 'red', 'blue', 'pink'))

# Input: 'red green blue', 'red', 'blue', 'pink'
# Output: True
print(check_input_output('red green blue', 'red', 'blue', 'pink'))

# End time: 2024-03-30 05:07:20.316136
# Elapsed time in seconds: 3.5705422930004715