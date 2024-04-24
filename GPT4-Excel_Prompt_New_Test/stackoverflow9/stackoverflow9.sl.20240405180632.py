# Start time: 2024-04-05 18:32:32.419713

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return last word/phrase from input, and input as ['Sarah Jane Jones'] output is Jones, input as ['Bob Jane Smithfield'] output is Smithfield, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(input_string):
    # Split the input string by spaces to get all words/phrases
    words = input_string.split()
    # Return the last word/phrase from the split input string
    return words[-1]

# Test cases
result1 = generated_function('Sarah Jane Jones')
result2 = generated_function('Bob Jane Smithfield')

# The outputs can be checked against the expected results outside of this code
print(generated_function("Sarah Jane Jones"))  ## Output: Jones
print(generated_function("Bob Jane Smithfield"))  ## Output: Smithfield

# End time: 2024-04-05 18:32:35.750628
# Elapsed time in seconds: 3.3308602039996913


# APPEND TEST SCRIPTS...
print(generated_function("Sarah Jane Jones"))  ## Output: Jones
print(generated_function("Bob Jane Smithfield"))  ## Output: Smithfield


print(generated_function("Jones Jane Sarah"))  ### Output: Sarah
print(generated_function("Smithfield Jane Bob"))  ### Output: Bob

# TEST SCRIPTS APPENDED!

