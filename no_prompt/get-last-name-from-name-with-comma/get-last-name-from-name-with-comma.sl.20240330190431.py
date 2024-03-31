# Start time: 2024-03-30 19:06:42.773944

# Content: Given that given input as ['chang,amy'] output is amy,chang, given input as ['smith,bobby'] output is bobby,smith, given input as ['lennox,aaron'] output is aaron,lennox, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: 'chang,amy'
# Output: 'amy,chang'

def reverse_name(input_str):
    try:
        # Split the input string by comma
        names = input_str.split(',')
        
        # Reverse the order of names and join them with a comma
        reversed_names = ','.join(reversed(names))
        
        return reversed_names
    except Exception as e:
        return str(e)

# Test cases
print(reverse_name('chang,amy'))  # Output: 'amy,chang'
print(reverse_name('smith,bobby'))  # Output: 'bobby,smith'
print(reverse_name('lennox,aaron'))  # Output: 'aaron,lennox'

# End time: 2024-03-30 19:06:44.200711
# Elapsed time in seconds: 1.4267241770003238