# Start time: 2024-03-30 00:03:43.846256
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: if the second, third, and fourth inputs (words) are in the first input (expression), then return true, else false, and given input as ['yellow dog on green grass', 'yellow', 'green', 'dog'] output is true, given input as ['Lone dog with a green frisbie on yellow sand', 'yellow', 'green', 'dog'] output is true, given input as ['A yellow sun in a green field', 'yellow', 'green', 'dog'] output is false, given input as ['yellow neon sign with a green background', 'yellow', 'green', 'dog'] output is false, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: if the second, third, and fourth inputs (words) are in the first input (expression), then return true, else false
# Input: ['yellow dog on green grass', 'yellow', 'green', 'dog']
# Output: true

def check_words(expression, word1, word2, word3):
    try:
        words = expression.split()
        if word1 in words and word2 in words and word3 in words:
            return True
        else:
            return False
    except Exception as e:
        print("An error occurred:", e)
        return False

# Test cases
print(check_words('yellow dog on green grass', 'yellow', 'green', 'dog'))  # Output: true
print(check_words('Lone dog with a green frisbie on yellow sand', 'yellow', 'green', 'dog'))  # Output: true
print(check_words('A yellow sun in a green field', 'yellow', 'green', 'dog'))  # Output: false
print(check_words('yellow neon sign with a green background', 'yellow', 'green', 'dog'))  # Output: false

# End time: 2024-03-30 00:03:51.274745
# Elapsed time in seconds: 7.4282704170000216