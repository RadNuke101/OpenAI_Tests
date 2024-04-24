# Start time: 2024-04-05 17:25:06.835258

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return last word/phrase from input, and input as ['Sarah Jane Jones'] output is Jones, input as ['Bob Jane Smithfield'] output is Smithfield, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(*args):
    # Initialize an empty list to store the results
    results = []
    
    # Iterate through each argument provided
    for arg in args:
        # Split the argument into words and append the last word to the results list
        results.append(arg.split()[-1])
    
    # If there's only one result, return it directly; otherwise, return the list of results
    return results[0] if len(results) == 1 else results

# Test cases
print(generated_function('Sarah Jane Jones'))  # Expected output: Jones
print(generated_function('Bob Jane Smithfield'))  # Expected output: Smithfield
print(generated_function("Sarah Jane Jones"))  ## Output: Jones
print(generated_function("Bob Jane Smithfield"))  ## Output: Smithfield

# End time: 2024-04-05 17:25:10.836073
# Elapsed time in seconds: 4.00070790799964


# APPEND TEST SCRIPTS...
print(generated_function("Sarah Jane Jones"))  ## Output: Jones
print(generated_function("Bob Jane Smithfield"))  ## Output: Smithfield


print(generated_function("Jones Jane Sarah"))  ### Output: Sarah
print(generated_function("Smithfield Jane Bob"))  ### Output: Bob

# TEST SCRIPTS APPENDED!

