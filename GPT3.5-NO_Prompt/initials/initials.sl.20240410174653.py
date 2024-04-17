# Start time: 2024-04-10 17:49:07.131587

'''
Prompt:
Given that input as ['Nancy FreeHafer'] output is N.F., input as ['Andrew Cencici'] output is A.C., input as ['Jan Kotas'] output is J.K., input as ['Mariya Sergienko'] output is M.S., , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        name_parts = input_str.split()
        first_name = name_parts[0][0].upper()
        last_name = name_parts[1][0].upper()
        return f"{first_name}.{last_name}."
    except (IndexError, AttributeError):
        return "Invalid input format."

# Test cases
print(generated_function('Nancy FreeHafer'))  # Output: N.F.
print(generated_function('Andrew Cencici'))   # Output: A.C.
print(generated_function('Jan Kotas'))         # Output: J.K.
print(generated_function('Mariya Sergienko'))  # Output: M.S.
print(generated_function("Nancy FreeHafer"))  ## Output: N.F.
print(generated_function("Andrew Cencici"))  ## Output: A.C.
print(generated_function("Jan Kotas"))  ## Output: J.K.
print(generated_function("Mariya Sergienko"))  ## Output: M.S.

# End time: 2024-04-10 17:49:08.906730
# Elapsed time in seconds: 1.7750982229999863