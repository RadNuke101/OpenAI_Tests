# Start time: 2024-03-30 04:11:01.237324
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: if the second, third, and fourth inputs (words) are in the first input (expression), then return true, else false, and given input as ['yellow dog on green grass', 'yellow', 'green', 'dog'] output is true, given input as ['Lone dog with a green frisbie on yellow sand', 'yellow', 'green', 'dog'] output is true, given input as ['A yellow sun in a green field', 'yellow', 'green', 'dog'] output is false, given input as ['yellow neon sign with a green background', 'yellow', 'green', 'dog'] output is false, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
def check_inputs(expression, word1, word2, word3):
    try:
        words = expression.split()
        if word1 in words and word2 in words and word3 in words:
            return "true"
        else:
            return "false"
    except AttributeError:
        return "Invalid input format"

# Input: ['yellow dog on green grass', 'yellow', 'green', 'dog']
# Output: true
# Prompt: if the second, third, and fourth inputs (words) are in the first input (expression), then return true, else false

# Input: ['Lone dog with a green frisbie on yellow sand', 'yellow', 'green', 'dog']
# Output: true

# Input: ['A yellow sun in a green field', 'yellow', 'green', 'dog']
# Output: false

# Input: ['yellow neon sign with a green background', 'yellow', 'green', 'dog']
# Output: false

# End time: 2024-03-30 04:11:06.765156
# Elapsed time in seconds: 5.527484182999615