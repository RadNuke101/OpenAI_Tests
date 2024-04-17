# Start time: 2024-04-10 17:43:24.995531

'''
Prompt:
Given that input as ['Nancy FreeHafer'] output is Dr. Nancy, input as ['Andrew Cencici'] output is Dr. Andrew, input as ['Jan Kotas'] output is Dr. Jan, input as ['Mariya Sergienko'] output is Dr. Mariya, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        name = input_str.split()[0]
        return "Dr. " + name
    except:
        return "Invalid input"

# Test cases
print(generated_function('Nancy FreeHafer'))
print(generated_function('Andrew Cencici'))
print(generated_function('Jan Kotas'))
print(generated_function('Mariya Sergienko'))
print(generated_function("Nancy FreeHafer"))  ## Output: Dr. Nancy
print(generated_function("Andrew Cencici"))  ## Output: Dr. Andrew
print(generated_function("Jan Kotas"))  ## Output: Dr. Jan
print(generated_function("Mariya Sergienko"))  ## Output: Dr. Mariya

# End time: 2024-04-10 17:43:26.341598
# Elapsed time in seconds: 1.3460496430000148