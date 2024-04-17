# Start time: 2024-04-10 15:29:29.707333

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Input Column Summary:
- The input column data consists of full names in the format of [First Name Last Name].
- The names in the input column seem to be of Asian origin, with common surnames like Park, Kim, and Lee.

Output Column Summary:
- The output column consists of only the last names extracted from the input column data.
- The last names in the output column are predominantly Asian surnames like Kim and Lee.

Relationship Summary:
- The relationship between the input and output columns is that the output column specifically extracts and displays the last names from the input column data.
- The last names in the output column are typically common Asian surnames found in the input data, such as Kim and Lee.
- This suggests that the output column serves to isolate and highlight the shared cultural or familial identities represented by the last names in the input data., and input as ['Park Kim'] output is Kim, input as ['Lee Kim'] output is Kim, input as ['Kim Lee'] output is Lee, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the generated function
def generated_function(*args):
    output = []
    for name in args:
        last_name = name.split()[-1]
        output.append(last_name)
    return output

# Test cases
print(generated_function('Park Kim'))  # Output: ['Kim']
print(generated_function('Lee Kim'))  # Output: ['Kim']
print(generated_function('Kim Lee'))  # Output: ['Lee']
print(generated_function("Park Kim"))  ## Output: Kim
print(generated_function("Lee Kim"))  ## Output: Kim
print(generated_function("Kim Lee"))  ## Output: Lee

# End time: 2024-04-10 15:29:31.165454
# Elapsed time in seconds: 1.4580961080000634