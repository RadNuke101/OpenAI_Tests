# Start time: 2024-04-10 15:19:23.807195

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Summary for Input Column Data:
- The input column data consists of full names of individuals, with each name having a first name and a last name.

Summary for Output Column:
- The output column consists of abbreviated names, with only the first initial of the first name followed by the last name.

Relationship between Input and Output:
- The relationship between the input and output is that the output column takes the first initial of the first name from the input column and combines it with the last name to create an abbreviated name. This process simplifies the full names into shorter, more concise versions for easier reference or identification., and input as ['John Doe'] output is J Doe, input as ['Mayur Naik'] output is M Naik, input as ['Nimit Singh'] output is N Singh, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(*args):
    result = []
    for name in args:
        first_name, last_name = name.split()
        abbreviated_name = f"{first_name[0]} {last_name}"
        result.append(abbreviated_name)
    return result
print(generated_function("John Doe"))  ## Output: J Doe
print(generated_function("Mayur Naik"))  ## Output: M Naik
print(generated_function("Nimit Singh"))  ## Output: N Singh

# End time: 2024-04-10 15:19:24.719416
# Elapsed time in seconds: 0.9122743359998822