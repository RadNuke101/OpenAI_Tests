# Start time: 2024-04-10 18:13:38.469528

'''
Prompt:
Given that input as ['Susan Ann Chang'] output is Susan, input as ['Ayako Tanaka'] output is Ayako, input as ['Bobby T. smth'] output is Bobby, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        name = input_str.split()[0]
        return name
    except:
        return "Invalid input"

# Test cases
print(generated_function('Susan Ann Chang'))
print(generated_function('Ayako Tanaka'))
print(generated_function('Bobby T. smth'))
print(generated_function("Susan Ann Chang"))  ## Output: Susan
print(generated_function("Ayako Tanaka"))  ## Output: Ayako
print(generated_function("Bobby T. smth"))  ## Output: Bobby

# End time: 2024-04-10 18:13:39.552767
# Elapsed time in seconds: 1.083217427999898


# APPEND TEST SCRIPTS...
print(generated_function("Susan Ann Chang"))  ## Output: Susan
print(generated_function("Ayako Tanaka"))  ## Output: Ayako
print(generated_function("Bobby T. smth"))  ## Output: Bobby


print(generated_function("Jackson Ann Turner"))  ### Output: Jackson
print(generated_function("Olivia Tanaka Parker"))  ### Output: Olivia
print(generated_function("Benjamin T. Hayes"))  ### Output: Benjamin

# TEST SCRIPTS APPENDED!

