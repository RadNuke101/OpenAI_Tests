# Start time: 2024-04-10 16:12:35.276445

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Summary for Input Column Data:
- The input column data consists of full names in the format of [First Name Last Name].
- The names in the input column data are in a random order with no specific pattern.

Summary for Output Column Data:
- The output column data consists of last names extracted from the input column data.
- The last names in the output column data are consistently extracted from the last part of the full names in the input column data.

Relationship between Input and Output:
- The relationship between the input and output is that the last names in the output column are extracted from the last part of the full names in the input column data.
- The output column data provides a consistent pattern of last names, regardless of the order of the full names in the input column data., and input as ['Park Kim'] output is Kim, input as ['Lee Kim'] output is Kim, input as ['Kim Lee'] output is Lee, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the generated function
def generated_function(*args):
    output = []
    for name in args:
        last_name = name.split()[-1]
        output.append(last_name)
    return output

# Test cases
generated_function('Park Kim', 'Lee Kim', 'Kim Lee')
print(generated_function("Park Kim"))  ## Output: Kim
print(generated_function("Lee Kim"))  ## Output: Kim
print(generated_function("Kim Lee"))  ## Output: Lee

# End time: 2024-04-10 16:12:36.378208
# Elapsed time in seconds: 1.1017335450005703