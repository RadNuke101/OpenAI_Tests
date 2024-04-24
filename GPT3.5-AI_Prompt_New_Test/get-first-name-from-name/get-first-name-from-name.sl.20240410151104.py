# Start time: 2024-04-10 15:18:14.926778

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Input Column Summary:
- The input column data consists of names in various formats, including full names, names with middle initials, and names with suffixes.

Output Column Summary:
- The output column data consists of the first names extracted from the input names.

Relationship Summary:
- The relationship between the input and output columns is that the output column only retains the first names from the input names. This process involves extracting the first name from the input data, regardless of the format in which the name is presented. The output provides a simplified version of the input data by focusing on the first names only., and input as ['Susan Ann Chang'] output is Susan, input as ['Ayako Tanaka'] output is Ayako, input as ['Bobby T. smth'] output is Bobby, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the generated function
def generated_function(*args):
    output = []
    for name in args:
        first_name = name.split()[0]
        output.append(first_name)
    return output

# Test cases
print(generated_function('Susan Ann Chang'))  # Output: ['Susan']
print(generated_function('Ayako Tanaka'))  # Output: ['Ayako']
print(generated_function('Bobby T. Smith'))  # Output: ['Bobby']
print(generated_function("Susan Ann Chang"))  ## Output: Susan
print(generated_function("Ayako Tanaka"))  ## Output: Ayako
print(generated_function("Bobby T. smth"))  ## Output: Bobby

# End time: 2024-04-10 15:18:16.778292
# Elapsed time in seconds: 1.8514708150000843


# APPEND TEST SCRIPTS...
print(generated_function("Susan Ann Chang"))  ## Output: Susan
print(generated_function("Ayako Tanaka"))  ## Output: Ayako
print(generated_function("Bobby T. smth"))  ## Output: Bobby


print(generated_function("Jackson Ann Turner"))  ### Output: Jackson
print(generated_function("Olivia Tanaka Parker"))  ### Output: Olivia
print(generated_function("Benjamin T. Hayes"))  ### Output: Benjamin

# TEST SCRIPTS APPENDED!

