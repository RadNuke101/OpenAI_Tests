# Start time: 2024-04-10 17:50:39.144584

'''
Prompt:
Given that input as ['Susan Ann Chang'] output is Susan, input as ['Ayako Tanaka'] output is Ayako, input as ['Bobby T. smth'] output is Bobby, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(name):
    try:
        # Split the input name by space
        name_parts = name.split()
        
        # Check if the name has more than one part
        if len(name_parts) > 1:
            # Return the first part of the name
            return name_parts[0]
        else:
            # Return the entire name if it has only one part
            return name
    except AttributeError:
        return "Invalid input. Please provide a valid name as a string."

# Test cases
print(generated_function('Susan Ann Chang'))
print(generated_function('Ayako Tanaka'))
print(generated_function('Bobby T. smth'))
print(generated_function("Susan Ann Chang"))  ## Output: Susan
print(generated_function("Ayako Tanaka"))  ## Output: Ayako
print(generated_function("Bobby T. smth"))  ## Output: Bobby

# End time: 2024-04-10 17:50:41.209434
# Elapsed time in seconds: 2.0647963960000197