# Start time: 2024-03-30 18:35:10.429509

# Content: Given that given input as ['Nancy FreeHafer'] output is Nancy, given input as ['Andrew Cencici'] output is Andrew, given input as ['Jan Kotas'] output is Jan, given input as ['Mariya Sergienko'] output is Mariya, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_first_name(name):
    try:
        # Input: 'Nancy FreeHafer'
        # Output: 'Nancy'
        return name.split()[0]
    except (AttributeError, IndexError):
        return "Invalid input"

# Test cases
print(extract_first_name('Nancy FreeHafer'))  # Nancy
print(extract_first_name('Andrew Cencici'))   # Andrew
print(extract_first_name('Jan Kotas'))        # Jan
print(extract_first_name('Mariya Sergienko')) # Mariya

# End time: 2024-03-30 18:35:11.716371
# Elapsed time in seconds: 1.2868261719999907