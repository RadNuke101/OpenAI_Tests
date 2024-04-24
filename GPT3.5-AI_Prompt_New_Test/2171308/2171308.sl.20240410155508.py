# Start time: 2024-04-10 16:03:57.906454

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Summary for Input Column Data:
- The input column data consists of full names in the format of 'First Name Last Name'.
- The names appear to be of individuals with diverse backgrounds and origins.

Summary for Output Column:
- The output column consists of abbreviated names in the format of 'First Initial Last Name'.
- The abbreviation process involves taking the first initial of the first name and combining it with the last name.

Relationship between Input and Output:
- The relationship between the input and output is that the output column provides a shortened version of the full names in the input column.
- The abbreviation process involves extracting the first initial of the first name and combining it with the last name to create a concise representation of the full name.
- This relationship allows for a more compact and efficient way of referencing individuals while still retaining their identity., and input as ['John Doe'] output is J Doe, input as ['Mayur Naik'] output is M Naik, input as ['Nimit Singh'] output is N Singh, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the generated function
def generated_function(*args):
    output = []
    for name in args:
        first_name, last_name = name.split()
        abbreviated_name = f"{first_name[0]} {last_name}"
        output.append(abbreviated_name)
    return output

# Test cases
print(generated_function('John Doe'))  # Output: ['J Doe']
print(generated_function('Mayur Naik'))  # Output: ['M Naik']
print(generated_function('Nimit Singh'))  # Output: ['N Singh']
print(generated_function("John Doe"))  ## Output: J Doe
print(generated_function("Mayur Naik"))  ## Output: M Naik
print(generated_function("Nimit Singh"))  ## Output: N Singh

# End time: 2024-04-10 16:03:59.685915
# Elapsed time in seconds: 1.7794280809994234


# APPEND TEST SCRIPTS...
print(generated_function("John Doe"))  ## Output: J Doe
print(generated_function("Mayur Naik"))  ## Output: M Naik
print(generated_function("Nimit Singh"))  ## Output: N Singh


print(generated_function("John Singh"))  ### Output: J Singh
print(generated_function("Mayur Doe"))  ### Output: M Doe
print(generated_function("Nimit Naik"))  ### Output: N Naik

# TEST SCRIPTS APPENDED!

