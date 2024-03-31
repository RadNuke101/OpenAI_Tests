# Start time: 2024-03-30 01:25:24.707449
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: if either the second, third, or fourth inputs (words) are in the first input (expression), return true, else false, and given input as ['yellow dog on green grass', 'yellow', 'green', 'dog'] output is true, given input as ['warm gray sweater', 'yellow', 'green', 'dog'] output is false, given input as ['A yellow sun in a green field', 'yellow', 'green', 'dog'] output is true, given input as ['yellow neon sign with a green background', 'yellow', 'green', 'dog'] output is true, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
def check_input_output(input_str):
    try:
        input_list = input_str.split(', ')
        expression = input_list[0]
        words = input_list[1:]

        for word in words:
            if word in expression:
                return 'true'
        
        return 'false'
    
    except Exception as e:
        return 'Error: Invalid input format'

# Prompt: if either the second, third, or fourth inputs (words) are in the first input (expression), return true, else false
# Input: ['yellow dog on green grass', 'yellow', 'green', 'dog']
# Output: true
# Input: ['warm gray sweater', 'yellow', 'green', 'dog']
# Output: false
# Input: ['A yellow sun in a green field', 'yellow', 'green', 'dog']
# Output: true
# Input: ['yellow neon sign with a green background', 'yellow', 'green', 'dog']
# Output: true

# Test the function with the provided inputs
print(check_input_output('yellow dog on green grass, yellow, green, dog'))  # Output: true
print(check_input_output('warm gray sweater, yellow, green, dog'))  # Output: false
print(check_input_output('A yellow sun in a green field, yellow, green, dog'))  # Output: true
print(check_input_output('yellow neon sign with a green background, yellow, green, dog'))  # Output: true

# End time: 2024-03-30 01:25:31.538635
# Elapsed time in seconds: 6.831065815999864