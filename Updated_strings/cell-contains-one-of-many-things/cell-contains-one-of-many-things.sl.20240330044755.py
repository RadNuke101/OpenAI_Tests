# Start time: 2024-03-30 04:58:20.610818
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: if either the second, third, or fourth inputs (words) are in the first input (expression), return true, else false, and given input as ['yellow dog on green grass', 'yellow', 'green', 'dog'] output is true, given input as ['warm gray sweater', 'yellow', 'green', 'dog'] output is false, given input as ['A yellow sun in a green field', 'yellow', 'green', 'dog'] output is true, given input as ['yellow neon sign with a green background', 'yellow', 'green', 'dog'] output is true, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: if either the second, third, or fourth inputs (words) are in the first input (expression), return true, else false
# Input: ['yellow dog on green grass', 'yellow', 'green', 'dog'] Output: true
# Input: ['warm gray sweater', 'yellow', 'green', 'dog'] Output: false
# Input: ['A yellow sun in a green field', 'yellow', 'green', 'dog'] Output: true
# Input: ['yellow neon sign with a green background', 'yellow', 'green', 'dog'] Output: true

def check_words(input_str, word1, word2, word3):
    try:
        words = input_str.split()
        if word1 in words or word2 in words or word3 in words:
            return True
        else:
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

# Test cases
print(check_words('yellow dog on green grass', 'yellow', 'green', 'dog'))  # Output: True
print(check_words('warm gray sweater', 'yellow', 'green', 'dog'))  # Output: False
print(check_words('A yellow sun in a green field', 'yellow', 'green', 'dog'))  # Output: True
print(check_words('yellow neon sign with a green background', 'yellow', 'green', 'dog'))  # Output: True

# End time: 2024-03-30 04:58:30.411771
# Elapsed time in seconds: 9.801170009999623