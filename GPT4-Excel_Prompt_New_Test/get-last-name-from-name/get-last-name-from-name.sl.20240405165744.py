# Start time: 2024-04-05 17:26:19.794796

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the second word of the inputted phrase, and input as ['Park Kim'] output is Kim, input as ['Lee Kim'] output is Kim, input as ['Kim Lee'] output is Lee, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(phrase):
    # Split the input phrase by spaces and return the second word
    return phrase.split()[1]

# Test cases
result1 = generated_function('Park Kim')
result2 = generated_function('Lee Kim')
result3 = generated_function('Kim Lee')

# The results can be printed or used as needed
print(generated_function("Park Kim"))  ## Output: Kim
print(generated_function("Lee Kim"))  ## Output: Kim
print(generated_function("Kim Lee"))  ## Output: Lee

# End time: 2024-04-05 17:26:22.236542
# Elapsed time in seconds: 2.4416793080008574


# APPEND TEST SCRIPTS...
print(generated_function("Park Kim"))  ## Output: Kim
print(generated_function("Lee Kim"))  ## Output: Kim
print(generated_function("Kim Lee"))  ## Output: Lee


print(generated_function("Benjamin Hayes"))  ### Output: Hayes
print(generated_function("Emma Reynolds"))  ### Output: Reynolds
print(generated_function("Grace Harrison"))  ### Output: Harrison
print(generated_function("Caleb Mitchell"))  ### Output: Mitchell
print(generated_function("Olivia Parker"))  ### Output: Parker
print(generated_function("Jackson Turner"))  ### Output: Turner

# TEST SCRIPTS APPENDED!

