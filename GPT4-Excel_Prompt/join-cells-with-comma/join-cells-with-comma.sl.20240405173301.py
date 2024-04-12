# Start time: 2024-04-05 17:33:01.551980

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: if the first input is not empty, return the first input followed by a comma and space, if the second input is not empty, return the second input followed by a comma and space, if the third input is not empty, return the third input , and input as ['figs', '', 'apples'] output is figs, apples, input as ['mangos', 'kiwis', 'grapes'] output is mangos, kiwis, grapes, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(first_input, second_input, third_input):
    # Initialize an empty string to store the result
    result = ""
    
    # Check if the first input is not empty
    if first_input:
        result += first_input + ", "
    
    # Check if the second input is not empty
    if second_input:
        result += second_input + ", "
    
    # Check if the third input is not empty
    if third_input:
        result += third_input
    
    # If the result ends with a comma and a space, remove them
    if result.endswith(", "):
        result = result[:-2]
    
    return result

# Test cases
print(generated_function('figs', '', 'apples'))  # Expected output: figs, apples
print(generated_function('mangos', 'kiwis', 'grapes'))  # Expected output: mangos, kiwis, grapes
print(generated_function("figs", "", "apples"))  ## Output: figs, apples
print(generated_function("mangos", "kiwis", "grapes"))  ## Output: mangos, kiwis, grapes

# End time: 2024-04-05 17:33:07.428379
# Elapsed time in seconds: 5.8762417429998095