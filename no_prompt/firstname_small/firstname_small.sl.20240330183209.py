# Start time: 2024-03-30 18:38:36.054905

# Content: Given that given input as ['Nancy FreeHafer'] output is Nancy, given input as ['Andrew Cencici'] output is Andrew, given input as ['Jan Kotas'] output is Jan, given input as ['Mariya Sergienko'] output is Mariya, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_first_name(full_name):
    try:
        # Input: 'Nancy FreeHafer'
        # Output: 'Nancy'
        
        # Input: 'Andrew Cencici'
        # Output: 'Andrew'
        
        # Input: 'Jan Kotas'
        # Output: 'Jan'
        
        # Input: 'Mariya Sergienko'
        # Output: 'Mariya'
        
        first_name = full_name.split()[0]
        return first_name
    except Exception as e:
        print("Error: {}".format(e))

# Test cases
print(extract_first_name('Nancy FreeHafer'))  # Output: Nancy
print(extract_first_name('Andrew Cencici'))   # Output: Andrew
print(extract_first_name('Jan Kotas'))        # Output: Jan
print(extract_first_name('Mariya Sergienko')) # Output: Mariya

# End time: 2024-03-30 18:38:38.094897
# Elapsed time in seconds: 2.039933285000018