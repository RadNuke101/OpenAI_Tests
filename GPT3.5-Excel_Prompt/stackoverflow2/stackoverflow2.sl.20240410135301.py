# Start time: 2024-04-10 14:03:04.503378

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: remove the last word/phrase from input, and input as ['india china japan'] output is india china, input as ['indonesia korea'] output is indonesia, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the generated function
def generated_function(*args):
    # Initialize an empty list to store the outputs
    outputs = []
    
    # Iterate through each input argument
    for arg in args:
        # Split the input argument into words
        words = arg.split()
        
        # Remove the last word
        words.pop()
        
        # Join the remaining words back into a string
        output = ' '.join(words)
        
        # Append the output to the list of outputs
        outputs.append(output)
    
    # Return the list of outputs
    return outputs

# Test cases
print(generated_function('india china japan'))
print(generated_function('indonesia korea'))
print(generated_function("india china japan"))  ## Output: india china
print(generated_function("indonesia korea"))  ## Output: indonesia

# End time: 2024-04-10 14:03:07.197645
# Elapsed time in seconds: 2.694218677999743