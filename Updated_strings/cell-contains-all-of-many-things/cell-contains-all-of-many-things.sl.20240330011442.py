# Start time: 2024-03-30 01:30:36.507178
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: if the second, third, and fourth inputs (words) are in the first input (expression), then return true, else false, and given input as ['yellow dog on green grass', 'yellow', 'green', 'dog'] output is true, given input as ['Lone dog with a green frisbie on yellow sand', 'yellow', 'green', 'dog'] output is true, given input as ['A yellow sun in a green field', 'yellow', 'green', 'dog'] output is false, given input as ['yellow neon sign with a green background', 'yellow', 'green', 'dog'] output is false, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
def check_expression(input_str):
    try:
        input_list = input_str.split(', ')
        expression = input_list[0]
        words = input_list[1:]

        for word in words:
            if word not in expression:
                return 'false'

        return 'true'

    except Exception as e:
        return 'Invalid input'

# Prompt: if the second, third, and fourth inputs (words) are in the first input (expression), then return true, else false
# Input: 'yellow dog on green grass, yellow, green, dog'
# Output: true
# Input: 'Lone dog with a green frisbie on yellow sand, yellow, green, dog'
# Output: true
# Input: 'A yellow sun in a green field, yellow, green, dog'
# Output: false
# Input: 'yellow neon sign with a green background, yellow, green, dog'
# Output: false

# Test cases
print(check_expression('yellow dog on green grass, yellow, green, dog'))  # true
print(check_expression('Lone dog with a green frisbie on yellow sand, yellow, green, dog'))  # true
print(check_expression('A yellow sun in a green field, yellow, green, dog'))  # false
print(check_expression('yellow neon sign with a green background, yellow, green, dog'))  # false

# End time: 2024-03-30 01:30:43.349757
# Elapsed time in seconds: 6.842464275999191