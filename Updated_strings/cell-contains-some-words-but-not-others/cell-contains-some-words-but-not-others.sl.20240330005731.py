# Start time: 2024-03-30 00:58:34.655777
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: if the second input (word) is in the first input (expresssion), return true, else false, and given input as ['red ball, green sweater', 'red', 'green', 'pink'] output is true, given input as ['pink ball, green sweater', 'red', 'green', 'pink'] output is false, given input as ['blue sea, pink ribbon', 'red', 'blue', 'pink'] output is false, given input as ['black sea, white ribbon', 'red', 'blue', 'pink'] output is false, given input as ['red green blue', 'red', 'blue', 'pink'] output is true, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: if the second input (word) is in the first input (expression), return true, else false
# Input: ['red ball, green sweater', 'red', 'green', 'pink']
# Output: true

def check_word_in_expression(expression, *words):
    try:
        for word in words:
            if word in expression:
                return True
        return False
    except TypeError:
        print("Invalid input format")
        return False

# Test cases
print(check_word_in_expression('red ball, green sweater', 'red', 'green', 'pink'))  # Output: True
print(check_word_in_expression('pink ball, green sweater', 'red', 'green', 'pink'))  # Output: False
print(check_word_in_expression('blue sea, pink ribbon', 'red', 'blue', 'pink'))  # Output: False
print(check_word_in_expression('black sea, white ribbon', 'red', 'blue', 'pink'))  # Output: False
print(check_word_in_expression('red green blue', 'red', 'blue', 'pink'))  # Output: True

# End time: 2024-03-30 00:58:39.020946
# Elapsed time in seconds: 4.365044091000527