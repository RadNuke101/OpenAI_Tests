# Start time: 2024-03-30 04:44:37.336226
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: if only one of the inputs from the second, third, or fourth column are in the first two words of the first input (first column), return true, else false, and given input as ['yellow dog on green grass', 'yellow', 'green', 'cat'] output is true, given input as ['warm gray sweater', 'yellow', 'green', 'cat'] output is false, given input as ['blue neon signs', 'blue', 'green', 'neon'] output is false, given input as ['hot pink socks', 'blue', 'pink', 'neon'] output is true, given input as ['deep black eyes', 'yellow', 'green', 'neon'] output is false, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: if only one of the inputs from the second, third, or fourth column are in the first two words of the first input, return true, else false
# Input: ['yellow dog on green grass', 'yellow', 'green', 'cat'] Output: true
# Input: ['warm gray sweater', 'yellow', 'green', 'cat'] Output: false
# Input: ['blue neon signs', 'blue', 'green', 'neon'] Output: false
# Input: ['hot pink socks', 'blue', 'pink', 'neon'] Output: true
# Input: ['deep black eyes', 'yellow', 'green', 'neon'] Output: false

def check_input_match(input_str, word1, word2, word3):
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
    except Exception as e:
        print(f"Error: {e}")
        return False

# Test cases
print(check_input_match('yellow dog on green grass', 'yellow', 'green', 'cat'))  # Output: True
print(check_input_match('warm gray sweater', 'yellow', 'green', 'cat'))  # Output: False
print(check_input_match('blue neon signs', 'blue', 'green', 'neon'))  # Output: False
print(check_input_match('hot pink socks', 'blue', 'pink', 'neon'))  # Output: True
print(check_input_match('deep black eyes', 'yellow', 'green', 'neon'))  # Output: False

# End time: 2024-03-30 04:44:45.657746
# Elapsed time in seconds: 8.321473700998467