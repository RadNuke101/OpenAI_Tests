# Start time: 2024-04-05 16:14:47.197073

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
    # Return the results list if there are multiple results, otherwise return the single result
    return results if len(results) > 1 else results[0]

# Test cases
result1 = generated_function('Sarah Jane Jones')
result2 = generated_function('Bob Jane Smithfield')

# Since the prompt specifies not to include the output of the test code, these lines are commented out
# print(result1)
# print(result2)
print(generated_function("Sarah Jane Jones"))  ## Output: Jones
print(generated_function("Bob Jane Smithfield"))  ## Output: Smithfield

# End time: 2024-04-05 16:14:52.111887
# Elapsed time in seconds: 4.914675223999893


# APPEND TEST SCRIPTS...
print(generated_function("Sarah Jane Jones"))  ## Output: Jones
print(generated_function("Bob Jane Smithfield"))  ## Output: Smithfield


print(generated_function("Jones Jane Sarah"))  ### Output: Sarah
print(generated_function("Smithfield Jane Bob"))  ### Output: Bob

# TEST SCRIPTS APPENDED!

