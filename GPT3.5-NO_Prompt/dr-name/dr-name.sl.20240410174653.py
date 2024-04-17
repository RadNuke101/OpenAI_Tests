# Start time: 2024-04-10 17:51:09.019774

'''
Prompt:
Given that input as ['Nancy FreeHafer'] output is Dr. Nancy, input as ['Andrew Cencici'] output is Dr. Andrew, input as ['Jan Kotas'] output is Dr. Jan, input as ['Mariya Sergienko'] output is Dr. Mariya, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(name):
    try:
        # Split the input name into first name and last name
        first_name, last_name = name.split()
        
        # Check if the last name contains 'FreeHafer'
        if 'FreeHafer' in last_name:
            return 'Dr. ' + first_name
        else:
            return 'Dr. ' + first_name
    except ValueError:
        return 'Invalid input format'

# Test cases
print(generated_function('Nancy FreeHafer'))  # Output: Dr. Nancy
print(generated_function('Andrew Cencici'))    # Output: Dr. Andrew
print(generated_function('Jan Kotas'))         # Output: Dr. Jan
print(generated_function('Mariya Sergienko'))  # Output: Dr. Mariya
print(generated_function("Nancy FreeHafer"))  ## Output: Dr. Nancy
print(generated_function("Andrew Cencici"))  ## Output: Dr. Andrew
print(generated_function("Jan Kotas"))  ## Output: Dr. Jan
print(generated_function("Mariya Sergienko"))  ## Output: Dr. Mariya

# End time: 2024-04-10 17:51:11.733644
# Elapsed time in seconds: 2.7137980099998913