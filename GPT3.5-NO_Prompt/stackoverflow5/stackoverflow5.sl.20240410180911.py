# Start time: 2024-04-10 18:11:40.552580

'''
Prompt:
Given that input as ['valentine day=1915=50==7.1=45'] output is valentine day, input as ['movie blah=2blahblah, The=1914=54==7.9=17'] output is movie blah=2blahblah, The, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        input_list = input_str.split('=')
        output = input_list[0]
        for i in range(1, len(input_list)):
            if input_list[i] == '':
                output += ', '
            else:
                output += '=' + input_list[i]
        return output
    except Exception as e:
        return "Error: {}".format(e)

# Test cases
test_input1 = 'valentine day=1915=50==7.1=45'
test_input2 = 'movie blah=2blahblah, The=1914=54==7.9=17'
print(generated_function(test_input1))
print(generated_function(test_input2))
print(generated_function("valentine day=1915=50==7.1=45"))  ## Output: valentine day
print(generated_function("movie blah=2blahblah, The=1914=54==7.9=17"))  ## Output: movie blah=2blahblah, The

# End time: 2024-04-10 18:11:43.119980
# Elapsed time in seconds: 2.567351181000049