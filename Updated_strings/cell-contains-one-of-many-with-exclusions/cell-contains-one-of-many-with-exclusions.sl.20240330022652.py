# Start time: 2024-03-30 02:42:27.024253
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: if only one of the inputs from the second, third, or fourth column are in the first two words of the first input (first column), return true, else false, and given input as ['yellow dog on green grass', 'yellow', 'green', 'cat'] output is true, given input as ['warm gray sweater', 'yellow', 'green', 'cat'] output is false, given input as ['blue neon signs', 'blue', 'green', 'neon'] output is false, given input as ['hot pink socks', 'blue', 'pink', 'neon'] output is true, given input as ['deep black eyes', 'yellow', 'green', 'neon'] output is false, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
def check_inputs(input_str, first_word, second_word, third_word):
    try:
        input_list = input_str.split()
        first_two_words = input_list[:2]
        
        if second_word in first_two_words or third_word in first_two_words:
            return 'true'
        else:
            return 'false'
    except:
        return 'Invalid input'

# Prompt: if only one of the inputs from the second, third, or fourth column are in the first two words of the first input (first column), return true, else false
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

# End time: 2024-03-30 02:42:31.321265
# Elapsed time in seconds: 4.296914096999899