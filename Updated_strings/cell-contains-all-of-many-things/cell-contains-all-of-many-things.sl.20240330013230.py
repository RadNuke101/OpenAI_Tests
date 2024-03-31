# Start time: 2024-03-30 01:49:26.611183
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: if the second, third, and fourth inputs (words) are in the first input (expression), then return true, else false, and given input as ['yellow dog on green grass', 'yellow', 'green', 'dog'] output is true, given input as ['Lone dog with a green frisbie on yellow sand', 'yellow', 'green', 'dog'] output is true, given input as ['A yellow sun in a green field', 'yellow', 'green', 'dog'] output is false, given input as ['yellow neon sign with a green background', 'yellow', 'green', 'dog'] output is false, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
def check_input(expression, word1, word2, word3):
    try:
        if word1 in expression and word2 in expression and word3 in expression:
            return "true"
        else:
            return "false"
    except:
        return "Invalid input"

# Prompt: if the second, third, and fourth inputs (words) are in the first input (expression), then return true, else false
# Input: ['yellow dog on green grass', 'yellow', 'green', 'dog']
# Output: true
print(check_input('yellow dog on green grass', 'yellow', 'green', 'dog'))

# Input: ['Lone dog with a green frisbie on yellow sand', 'yellow', 'green', 'dog']
# Output: true
print(check_input('Lone dog with a green frisbie on yellow sand', 'yellow', 'green', 'dog'))

# Input: ['A yellow sun in a green field', 'yellow', 'green', 'dog']
# Output: false
print(check_input('A yellow sun in a green field', 'yellow', 'green', 'dog'))

# Input: ['yellow neon sign with a green background', 'yellow', 'green', 'dog']
# Output: false
print(check_input('yellow neon sign with a green background', 'yellow', 'green', 'dog'))

# End time: 2024-03-30 01:49:31.240868
# Elapsed time in seconds: 4.629609704999893