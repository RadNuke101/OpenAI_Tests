# Start time: 2024-03-30 01:07:08.368103
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the nth word in the inputted expression, with n being the second input, and given input as ['you can do anything but you cant do everything.', '4'] output is anything, given input as ['you can do anything but you cant do everything.', '1'] output is you, given input as ['you can do anything but you cant do everything.', '2'] output is can, given input as ['you can do anything but you cant do everything.', '3'] output is do, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return the nth word in the inputted expression, with n being the second input
# Input: ['you can do anything but you cant do everything.', '4']
# Output: anything

def get_nth_word(input_str, n):
    try:
        words = input_str.split()
        return words[int(n) - 1]
    except (IndexError, ValueError):
        return "Invalid input"

# Test cases
input_1 = 'you can do anything but you cant do everything.'
n_1 = '4'
print(get_nth_word(input_1, n_1))  # Output: anything

input_2 = 'you can do anything but you cant do everything.'
n_2 = '1'
print(get_nth_word(input_2, n_2))  # Output: you

input_3 = 'you can do anything but you cant do everything.'
n_3 = '2'
print(get_nth_word(input_3, n_3))  # Output: can

input_4 = 'you can do anything but you cant do everything.'
n_4 = '3'
print(get_nth_word(input_4, n_4))  # Output: do

# End time: 2024-03-30 01:07:11.865211
# Elapsed time in seconds: 3.4970171349996235