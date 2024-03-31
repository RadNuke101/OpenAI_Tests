# Start time: 2024-03-30 00:21:01.288246
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: if the second, third, and fourth inputs (words) are in the first input (expression), then return true, else false, and given input as ['yellow dog on green grass', 'yellow', 'green', 'dog'] output is true, given input as ['Lone dog with a green frisbie on yellow sand', 'yellow', 'green', 'dog'] output is true, given input as ['A yellow sun in a green field', 'yellow', 'green', 'dog'] output is false, given input as ['yellow neon sign with a green background', 'yellow', 'green', 'dog'] output is false, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: if the second, third, and fourth inputs (words) are in the first input (expression), then return true, else false
# Input: ['yellow dog on green grass', 'yellow', 'green', 'dog'] 
# Output: true
# Input: ['Lone dog with a green frisbie on yellow sand', 'yellow', 'green', 'dog'] 
# Output: true
# Input: ['A yellow sun in a green field', 'yellow', 'green', 'dog'] 
# Output: false
# Input: ['yellow neon sign with a green background', 'yellow', 'green', 'dog'] 
# Output: false

def check_words_in_expression(expression, word1, word2, word3):
    try:
        words = [word1, word2, word3]
        for word in words:
            if word not in expression:
                return False
        return True
    except Exception as e:
        return f"Error: {e}"

# Test cases
print(check_words_in_expression('yellow dog on green grass', 'yellow', 'green', 'dog'))  # Output: True
print(check_words_in_expression('Lone dog with a green frisbie on yellow sand', 'yellow', 'green', 'dog'))  # Output: True
print(check_words_in_expression('A yellow sun in a green field', 'yellow', 'green', 'dog'))  # Output: False
print(check_words_in_expression('yellow neon sign with a green background', 'yellow', 'green', 'dog'))  # Output: False

# End time: 2024-03-30 00:21:09.600565
# Elapsed time in seconds: 8.312275901000248