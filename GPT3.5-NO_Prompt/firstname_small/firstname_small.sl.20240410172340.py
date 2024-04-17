# Start time: 2024-04-10 17:27:34.607650

'''
Prompt:
Given that input as ['Nancy FreeHafer'] output is Nancy, input as ['Andrew Cencici'] output is Andrew, input as ['Jan Kotas'] output is Jan, input as ['Mariya Sergienko'] output is Mariya, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        name = input_str.split()[0]
        return name
    except Exception as e:
        return "Invalid input"

# Test cases
print(generated_function('Nancy FreeHafer'))  # Output: Nancy
print(generated_function('Andrew Cencici'))    # Output: Andrew
print(generated_function('Jan Kotas'))         # Output: Jan
print(generated_function('Mariya Sergienko'))  # Output: Mariya
print(generated_function("Nancy FreeHafer"))  ## Output: Nancy
print(generated_function("Andrew Cencici"))  ## Output: Andrew
print(generated_function("Jan Kotas"))  ## Output: Jan
print(generated_function("Mariya Sergienko"))  ## Output: Mariya

# End time: 2024-04-10 17:27:36.323131
# Elapsed time in seconds: 1.715442367999998