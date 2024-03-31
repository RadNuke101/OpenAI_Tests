# Start time: 2024-03-30 00:50:30.463246
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: if either the second, third, or fourth inputs (words) are in the first input (expression), return true, else false, and given input as ['yellow dog on green grass', 'yellow', 'green', 'dog'] output is true, given input as ['warm gray sweater', 'yellow', 'green', 'dog'] output is false, given input as ['A yellow sun in a green field', 'yellow', 'green', 'dog'] output is true, given input as ['yellow neon sign with a green background', 'yellow', 'green', 'dog'] output is true, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: if either the second, third, or fourth inputs (words) are in the first input (expression), return true, else false
# Input: ['yellow dog on green grass', 'yellow', 'green', 'dog']
# Output: true

def check_words(expression, word1, word2, word3):
    try:
        if word1 in expression or word2 in expression or word3 in expression:
            return True
        else:
            return False
    except Exception as e:
        print("Error:", e)
        return None

# Test cases
print(check_words('yellow dog on green grass', 'yellow', 'green', 'dog'))  # Output: True
print(check_words('warm gray sweater', 'yellow', 'green', 'dog'))  # Output: False
print(check_words('A yellow sun in a green field', 'yellow', 'green', 'dog'))  # Output: True
print(check_words('yellow neon sign with a green background', 'yellow', 'green', 'dog'))  # Output: True

# End time: 2024-03-30 00:50:33.833991
# Elapsed time in seconds: 3.370663937000245