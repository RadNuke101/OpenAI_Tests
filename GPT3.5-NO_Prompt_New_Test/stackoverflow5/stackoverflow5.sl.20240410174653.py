# Start time: 2024-04-10 17:49:04.827592

'''
Prompt:
Given that input as ['valentine day=1915=50==7.1=45'] output is valentine day, input as ['movie blah=2blahblah, The=1914=54==7.9=17'] output is movie blah=2blahblah, The, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        # Split the input string by '='
        parts = input_str.split('=')
        
        # Extract the first part as the output
        output = parts[0]
        
        # Check if there are additional parts
        if len(parts) > 1:
            # Append additional parts to the output
            for part in parts[1:]:
                output += '=' + part
        
        return output
    
    except Exception as e:
        return str(e)

# Test cases
test_input1 = 'valentine day=1915=50==7.1=45'
test_input2 = 'movie blah=2blahblah, The=1914=54==7.9=17'

print(generated_function(test_input1))
print(generated_function(test_input2))
print(generated_function("valentine day=1915=50==7.1=45"))  ## Output: valentine day
print(generated_function("movie blah=2blahblah, The=1914=54==7.9=17"))  ## Output: movie blah=2blahblah, The

# End time: 2024-04-10 17:49:07.056607
# Elapsed time in seconds: 2.2289567459999944


# APPEND TEST SCRIPTS...
print(generated_function("valentine day=1915=50==7.1=45"))  ## Output: valentine day
print(generated_function("movie blah=2blahblah, The=1914=54==7.9=17"))  ## Output: movie blah=2blahblah, The


print(generated_function("blah=2blahblah, alpha The=1914=54==7.9=17"))  ### Output: blah=2blahblah, alpha The
print(generated_function("day=1915=50==7.1=45"))  ### Output: day

# TEST SCRIPTS APPENDED!

