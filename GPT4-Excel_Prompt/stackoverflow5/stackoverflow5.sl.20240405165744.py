# Start time: 2024-04-05 17:06:26.101895

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return everything before the fifth occurance of "=" from the right of input, and input as ['valentine day=1915=50==7.1=45'] output is valentine day, input as ['movie blah=2blahblah, The=1914=54==7.9=17'] output is movie blah=2blahblah, The, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(input_string):
    # Split the input string by "=" and reverse the list to start counting from the right
    parts = input_string.split("=")[::-1]
    # Check if there are at least five "=" characters
    if len(parts) >= 5:
        # Join the parts excluding the first four occurrences of "=" from the right
        # and reverse back the result to its original order
        return "=".join(parts[4:][::-1])
    else:
        # If there are less than five "=" characters, return the whole string
        return input_string

# Test cases
print(generated_function('valentine day=1915=50==7.1=45'))  # Expected output: valentine day
print(generated_function('movie blah=2blahblah, The=1914=54==7.9=17'))  # Expected output: movie blah=2blahblah, The
print(generated_function("valentine day=1915=50==7.1=45"))  ## Output: valentine day
print(generated_function("movie blah=2blahblah, The=1914=54==7.9=17"))  ## Output: movie blah=2blahblah, The

# End time: 2024-04-05 17:06:31.471943
# Elapsed time in seconds: 5.3699478920007095