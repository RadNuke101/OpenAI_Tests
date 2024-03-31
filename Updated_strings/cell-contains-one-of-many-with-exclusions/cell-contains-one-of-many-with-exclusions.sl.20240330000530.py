# Start time: 2024-03-30 00:19:39.053026
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: if only one of the inputs from the second, third, or fourth column are in the first two words of the first input (first column), return true, else false, and given input as ['yellow dog on green grass', 'yellow', 'green', 'cat'] output is true, given input as ['warm gray sweater', 'yellow', 'green', 'cat'] output is false, given input as ['blue neon signs', 'blue', 'green', 'neon'] output is false, given input as ['hot pink socks', 'blue', 'pink', 'neon'] output is true, given input as ['deep black eyes', 'yellow', 'green', 'neon'] output is false, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: if only one of the inputs from the second, third, or fourth column are in the first two words of the first input, return true, else false
# Input: ['yellow dog on green grass', 'yellow', 'green', 'cat']
# Output: true
# Input: ['warm gray sweater', 'yellow', 'green', 'cat']
# Output: false
# Input: ['blue neon signs', 'blue', 'green', 'neon']
# Output: false
# Input: ['hot pink socks', 'blue', 'pink', 'neon']
# Output: true
# Input: ['deep black eyes', 'yellow', 'green', 'neon']
# Output: false

def check_inputs(input_str, word1, word2, word3):
    try:
        words = input_str.split()
        first_two_words = ' '.join(words[:2])
        
        count = 0
        if word1 in first_two_words:
            count += 1
        if word2 in first_two_words:
            count += 1
        if word3 in first_two_words:
            count += 1
        
        return count == 1
    except:
        return "Invalid input format"

# Test cases
print(check_inputs('yellow dog on green grass', 'yellow', 'green', 'cat'))  # Output: true
print(check_inputs('warm gray sweater', 'yellow', 'green', 'cat'))  # Output: false
print(check_inputs('blue neon signs', 'blue', 'green', 'neon'))  # Output: false
print(check_inputs('hot pink socks', 'blue', 'pink', 'neon'))  # Output: true
print(check_inputs('deep black eyes', 'yellow', 'green', 'neon'))  # Output: false

# End time: 2024-03-30 00:19:43.902199
# Elapsed time in seconds: 4.849146330999702