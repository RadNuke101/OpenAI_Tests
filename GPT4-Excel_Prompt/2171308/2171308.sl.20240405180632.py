# Start time: 2024-04-05 18:21:17.950756

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return first letter of first word, followed by a space, and then the second word, and input as ['John Doe'] output is J Doe, input as ['Mayur Naik'] output is M Naik, input as ['Nimit Singh'] output is N Singh, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(full_name):
    # Split the full name into first and second word
    parts = full_name.split()
    # Return the first letter of the first word, a space, and then the second word
    return parts[0][0] + " " + parts[1]

# Test cases
output1 = generated_function('John Doe')
output2 = generated_function('Mayur Naik')
output3 = generated_function('Nimit Singh')

# The outputs can be checked against the expected results
# Expected outputs are 'J Doe', 'M Naik', and 'N Singh' respectively
print(generated_function("John Doe"))  ## Output: J Doe
print(generated_function("Mayur Naik"))  ## Output: M Naik
print(generated_function("Nimit Singh"))  ## Output: N Singh

# End time: 2024-04-05 18:21:21.517740
# Elapsed time in seconds: 3.5668833480012836