# Start time: 2024-04-10 13:58:16.798491

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return first letter of first word, followed by a space, and then the second word, and input as ['John Doe'] output is J Doe, input as ['Mayur Naik'] output is M Naik, input as ['Nimit Singh'] output is N Singh, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the generated function
def generated_function(input_str):
    # Split the input string into two words
    words = input_str.split()
    
    # Return the first letter of the first word followed by a space and the second word
    return words[0][0] + " " + words[1]

# Test cases
print(generated_function('John Doe'))
print(generated_function('Mayur Naik'))
print(generated_function('Nimit Singh'))
print(generated_function("John Doe"))  ## Output: J Doe
print(generated_function("Mayur Naik"))  ## Output: M Naik
print(generated_function("Nimit Singh"))  ## Output: N Singh

# End time: 2024-04-10 13:58:18.862114
# Elapsed time in seconds: 2.0635875150001084