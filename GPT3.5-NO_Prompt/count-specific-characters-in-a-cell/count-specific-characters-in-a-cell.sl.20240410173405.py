# Start time: 2024-04-10 17:43:03.608358

'''
Prompt:
Given that input as ['Hannah', 'n'] output is 2, input as ['Hannah', 'x'] output is 0, input as ['Hannah', 'N'] output is 0, input as ['Hannah', 'a'] output is 2, input as ['Hannah', 'h'] output is 1, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        name = input_str[0]
        char = input_str[1].lower()
        
        count = name.lower().count(char)
        
        return count
    except IndexError:
        return "Input format is incorrect. Please provide a name and a character to search for."
    except AttributeError:
        return "Input format is incorrect. Please provide a name and a character to search for."

# Test cases
print(generated_function(['Hannah', 'n']))
print(generated_function(['Hannah', 'x']))
print(generated_function(['Hannah', 'N']))
print(generated_function(['Hannah', 'a']))
print(generated_function(['Hannah', 'h']))
print(generated_function("Hannah", "n"))  ## Output: 2
print(generated_function("Hannah", "x"))  ## Output: 0
print(generated_function("Hannah", "N"))  ## Output: 0
print(generated_function("Hannah", "a"))  ## Output: 2
print(generated_function("Hannah", "h"))  ## Output: 1

# End time: 2024-04-10 17:43:06.267362
# Elapsed time in seconds: 2.658970332999843