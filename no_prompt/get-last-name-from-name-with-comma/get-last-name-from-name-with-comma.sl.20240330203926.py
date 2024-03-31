# Start time: 2024-03-30 20:41:24.275844

# Content: Given that given input as ['chang,amy'] output is amy,chang, given input as ['smith,bobby'] output is bobby,smith, given input as ['lennox,aaron'] output is aaron,lennox, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def reverse_name(name):
    try:
        first_name, last_name = name.split(',')
        return f"{last_name},{first_name}"
    except ValueError:
        print("Invalid input format. Please provide input in the format 'lastname,firstname'.")

# Test cases
# Input: 'chang,amy'
# Output: 'amy,chang'
print(reverse_name('chang,amy'))

# Input: 'smith,bobby'
# Output: 'bobby,smith'
print(reverse_name('smith,bobby'))

# Input: 'lennox,aaron'
# Output: 'aaron,lennox'
print(reverse_name('lennox,aaron'))

# End time: 2024-03-30 20:41:26.006524
# Elapsed time in seconds: 1.7306336460005696