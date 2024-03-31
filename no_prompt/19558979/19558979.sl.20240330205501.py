# Start time: 2024-03-30 21:09:22.288702

# Content: Given that given input as ['spreadsheet', '1'] output is s, given input as ['spreadsheet', '2'] output is p, given input as ['spreadsheet', '3'] output is r, given input as ['spreadsheet', '4'] output is e, given input as ['spreadsheet', '5'] output is a, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: 'spreadsheet', '1'
# Output: s

def get_char(input_str, index_str):
    try:
        index = int(index_str)
        return input_str[index - 1]
    except ValueError:
        return "Invalid index, please provide a number."
    except IndexError:
        return "Index out of range."

# Test cases
print(get_char('spreadsheet', '1'))  # Output: s
print(get_char('spreadsheet', '2'))  # Output: p
print(get_char('spreadsheet', '3'))  # Output: r
print(get_char('spreadsheet', '4'))  # Output: e
print(get_char('spreadsheet', '5'))  # Output: a

# End time: 2024-03-30 21:09:23.683481
# Elapsed time in seconds: 1.3947533560003649