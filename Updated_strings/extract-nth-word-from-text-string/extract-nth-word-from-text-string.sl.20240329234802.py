# Start time: 2024-03-29 23:57:03.928683
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
print(get_nth_word('you can do anything but you cant do everything.', '4'))  # Output: anything
print(get_nth_word('you can do anything but you cant do everything.', '1'))  # Output: you
print(get_nth_word('you can do anything but you cant do everything.', '2'))  # Output: can
print(get_nth_word('you can do anything but you cant do everything.', '3'))  # Output: do

# End time: 2024-03-29 23:57:06.232465
# Elapsed time in seconds: 2.3036932019999767