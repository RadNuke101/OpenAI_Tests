# Start time: 2024-04-10 15:42:03.289663

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Summary for Input Column Data:
The input column data consists of full names of individuals. Each name is composed of a first name and a last name.

Summary for Output Column:
The output column consists of abbreviated names, where only the first letter of the first name is used followed by the full last name.

Relationship between Input and Output:
The relationship between the input and output is that the output column takes the first letter of the first name from the input column and combines it with the full last name. This results in a concise representation of the individual's name. The output column serves as a simplified version of the input column, providing a quick reference to the individual's identity., and input as ['John Doe'] output is J Doe, input as ['Mayur Naik'] output is M Naik, input as ['Nimit Singh'] output is N Singh, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(input_str):
    # Split the input string into first name and last name
    first_name, last_name = input_str.split()
    
    # Create the abbreviated name using the first letter of the first name and the full last name
    abbreviated_name = first_name[0] + ' ' + last_name
    
    return abbreviated_name

# Test cases
print(generated_function('John Doe'))
print(generated_function('Mayur Naik'))
print(generated_function('Nimit Singh'))
print(generated_function("John Doe"))  ## Output: J Doe
print(generated_function("Mayur Naik"))  ## Output: M Naik
print(generated_function("Nimit Singh"))  ## Output: N Singh

# End time: 2024-04-10 15:42:04.855421
# Elapsed time in seconds: 1.5657198320004682