# Start time: 2024-03-30 05:15:57.528916
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the nth word in the inputted expression, with n being the second input, and given input as ['you can do anything but you cant do everything.', '4'] output is anything, given input as ['you can do anything but you cant do everything.', '1'] output is you, given input as ['you can do anything but you cant do everything.', '2'] output is can, given input as ['you can do anything but you cant do everything.', '3'] output is do, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return the nth word in the inputted expression, with n being the second input
# Input: ['you can do anything but you cant do everything.', '4']
# Output: anything

def get_nth_word(input_str, n):
    try:
        words = input_str.split()
        nth_word = words[int(n) - 1]
        return nth_word
    except (IndexError, ValueError):
        return "Invalid input"

# Test cases
input1 = 'you can do anything but you cant do everything.'
n1 = '4'
print(get_nth_word(input1, n1))  # Output: anything

input2 = 'you can do anything but you cant do everything.'
n2 = '1'
print(get_nth_word(input2, n2))  # Output: you

input3 = 'you can do anything but you cant do everything.'
n3 = '2'
print(get_nth_word(input3, n3))  # Output: can

input4 = 'you can do anything but you cant do everything.'
n4 = '3'
print(get_nth_word(input4, n4))  # Output: do

# End time: 2024-03-30 05:16:02.086315
# Elapsed time in seconds: 4.55737912600307