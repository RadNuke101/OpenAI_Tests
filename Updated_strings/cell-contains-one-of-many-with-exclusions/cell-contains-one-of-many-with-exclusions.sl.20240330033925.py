# Start time: 2024-03-30 03:52:44.914817
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
        first_two_words = input_str.split()[:2]
        count = 0
        if word1 in first_two_words:
            count += 1
        if word2 in first_two_words:
            count += 1
        if word3 in first_two_words:
            count += 1
        
        return count == 1
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

# Test cases
print(check_inputs('yellow dog on green grass', 'yellow', 'green', 'cat'))  # Output: true
print(check_inputs('warm gray sweater', 'yellow', 'green', 'cat'))  # Output: false
print(check_inputs('blue neon signs', 'blue', 'green', 'neon'))  # Output: false
print(check_inputs('hot pink socks', 'blue', 'pink', 'neon'))  # Output: true
print(check_inputs('deep black eyes', 'yellow', 'green', 'neon'))  # Output: false

# End time: 2024-03-30 03:52:54.971121
# Elapsed time in seconds: 10.056006405000517