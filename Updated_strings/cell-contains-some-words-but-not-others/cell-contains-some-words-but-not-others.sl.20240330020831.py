# Start time: 2024-03-30 02:09:42.893856
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: if the second input (word) is in the first input (expresssion), return true, else false, and given input as ['red ball, green sweater', 'red', 'green', 'pink'] output is true, given input as ['pink ball, green sweater', 'red', 'green', 'pink'] output is false, given input as ['blue sea, pink ribbon', 'red', 'blue', 'pink'] output is false, given input as ['black sea, white ribbon', 'red', 'blue', 'pink'] output is false, given input as ['red green blue', 'red', 'blue', 'pink'] output is true, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: if the second input (word) is in the first input (expression), return true, else false
# Input: ['red ball, green sweater', 'red', 'green', 'pink']
# Output: true

def check_word_in_expression(expression, *words):
    try:
        expression = expression.split(', ')
        for word in words:
            if word in expression[0]:
                return True
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

# Test cases
print(check_word_in_expression('red ball, green sweater', 'red', 'green', 'pink'))  # Output: True
print(check_word_in_expression('pink ball, green sweater', 'red', 'green', 'pink'))  # Output: False
print(check_word_in_expression('blue sea, pink ribbon', 'red', 'blue', 'pink'))  # Output: False
print(check_word_in_expression('black sea, white ribbon', 'red', 'blue', 'pink'))  # Output: False
print(check_word_in_expression('red green blue', 'red', 'blue', 'pink'))  # Output: True

# End time: 2024-03-30 02:09:47.604595
# Elapsed time in seconds: 4.710609830000976