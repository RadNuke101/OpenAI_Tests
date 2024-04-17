# Start time: 2024-04-10 13:20:13.607785

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the first phrase in the inputted epxression that begins with "_", and input as ['this is a _username in the middle'] output is _username, input as ['twitter names look like= _name'] output is _name, input as ['with two _name1 and _name2'] output is _name1, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(*args):
    for arg in args:
        phrase = arg.split()[0]
        if phrase.startswith('_'):
            return phrase
print(generated_function("this is a _username in the middle"))  ## Output: _username
print(generated_function("twitter names look like= _name"))  ## Output: _name
print(generated_function("with two _name1 and _name2"))  ## Output: _name1

# End time: 2024-04-10 13:20:14.295710
# Elapsed time in seconds: 0.6879468020001696