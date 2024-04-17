# Start time: 2024-04-10 13:54:11.904104

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: take the first letter of the first input and add it to the front of the second input, then add "_" to the end, and then add the third input to the end, and input as ['ayako', 'ogawa', 'acme.com'] output is aogawa_acme.com, input as ['amy', 'johnson', 'google.com'] output is ajohnson_google.com, input as ['tom', 'chang', 'upenn.edu'] output is tchang_upenn.edu, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the function
def generated_function(input1, input2, input3):
    # Take the first letter of the first input
    first_letter = input1[0]
    
    # Add it to the front of the second input, then add "_" and the third input
    output = first_letter + input2 + "_" + input3
    
    return output

# Test cases
print(generated_function('ayako', 'ogawa', 'acme.com'))
print(generated_function('amy', 'johnson', 'google.com'))
print(generated_function('tom', 'chang', 'upenn.edu'))
print(generated_function("ayako", "ogawa", "acme.com"))  ## Output: aogawa_acme.com
print(generated_function("amy", "johnson", "google.com"))  ## Output: ajohnson_google.com
print(generated_function("tom", "chang", "upenn.edu"))  ## Output: tchang_upenn.edu

# End time: 2024-04-10 13:54:14.374303
# Elapsed time in seconds: 2.474113042999761