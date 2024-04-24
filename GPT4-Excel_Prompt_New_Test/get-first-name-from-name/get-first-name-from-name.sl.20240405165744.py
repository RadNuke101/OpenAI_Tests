# Start time: 2024-04-05 17:11:48.165562

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the first word of the inputted phrase, and input as ['Susan Ann Chang'] output is Susan, input as ['Ayako Tanaka'] output is Ayako, input as ['Bobby T. smth'] output is Bobby, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(phrase):
    # Split the input phrase by spaces and return the first word
    return phrase.split()[0]

# Test cases
print(generated_function('Susan Ann Chang'))  # Expected output: Susan
print(generated_function('Ayako Tanaka'))     # Expected output: Ayako
print(generated_function('Bobby T. smth'))    # Expected output: Bobby
print(generated_function("Susan Ann Chang"))  ## Output: Susan
print(generated_function("Ayako Tanaka"))  ## Output: Ayako
print(generated_function("Bobby T. smth"))  ## Output: Bobby

# End time: 2024-04-05 17:11:50.753436
# Elapsed time in seconds: 2.587800661000074


# APPEND TEST SCRIPTS...
print(generated_function("Susan Ann Chang"))  ## Output: Susan
print(generated_function("Ayako Tanaka"))  ## Output: Ayako
print(generated_function("Bobby T. smth"))  ## Output: Bobby


print(generated_function("Jackson Ann Turner"))  ### Output: Jackson
print(generated_function("Olivia Tanaka Parker"))  ### Output: Olivia
print(generated_function("Benjamin T. Hayes"))  ### Output: Benjamin

# TEST SCRIPTS APPENDED!

