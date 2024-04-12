# Start time: 2024-04-05 18:14:01.686959

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return everything before the fifth occurance of "=" from the right of input, and input as ['valentine day=1915=50==7.1=45'] output is valentine day, input as ['movie blah=2blahblah, The=1914=54==7.9=17'] output is movie blah=2blahblah, The, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(input_string):
    # Split the input string by "=" and reverse it to start counting from the right
    parts = input_string.split("=")[::-1]
    # If there are less than five "=", return the whole string as it is
    if len(parts) < 5:
        return input_string
    # Otherwise, join the parts after the fourth "=" from the right (fifth from the left when reversed)
    # and reverse it back to the original order
    return "=".join(parts[4:])[::-1]

# Test cases
print(generated_function('valentine day=1915=50==7.1=45'))  # Expected output: valentine day
print(generated_function('movie blah=2blahblah, The=1914=54==7.9=17'))  # Expected output: movie blah=2blahblah, The
print(generated_function("valentine day=1915=50==7.1=45"))  ## Output: valentine day
print(generated_function("movie blah=2blahblah, The=1914=54==7.9=17"))  ## Output: movie blah=2blahblah, The

# End time: 2024-04-05 18:14:06.055679
# Elapsed time in seconds: 4.368591937998644