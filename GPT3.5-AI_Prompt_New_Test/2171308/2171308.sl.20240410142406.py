# Start time: 2024-04-10 14:32:37.580714

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Summary for Input Column Data:
- The input column data consists of full names in the format of 'First Name Last Name'.
- Each entry in the input column represents a person's full name.

Summary for Output Column Data:
- The output column data consists of abbreviated names in the format of 'First Initial Last Name'.
- Each entry in the output column represents a person's abbreviated name.

Relationship between Input and Output:
- The relationship between the input and output columns is that the output column takes the first initial of the first name and combines it with the last name to create an abbreviated name.
- This process simplifies the full names into a more concise format while still retaining the individual's identity.
- The output column serves as a condensed version of the input column, making it easier to reference individuals quickly and efficiently., and input as ['John Doe'] output is J Doe, input as ['Mayur Naik'] output is M Naik, input as ['Nimit Singh'] output is N Singh, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the generated function
def generated_function(input_str):
    # Split the input string into first name and last name
    first_name, last_name = input_str.split()
    
    # Create the abbreviated name by taking the first initial of the first name and combining it with the last name
    abbreviated_name = first_name[0] + ' ' + last_name
    
    return abbreviated_name

# Test cases
print(generated_function('John Doe'))  # Output: J Doe
print(generated_function('Mayur Naik'))  # Output: M Naik
print(generated_function('Nimit Singh'))  # Output: N Singh
print(generated_function("John Doe"))  ## Output: J Doe
print(generated_function("Mayur Naik"))  ## Output: M Naik
print(generated_function("Nimit Singh"))  ## Output: N Singh

# End time: 2024-04-10 14:32:39.531410
# Elapsed time in seconds: 1.9506514849999803


# APPEND TEST SCRIPTS...
print(generated_function("John Doe"))  ## Output: J Doe
print(generated_function("Mayur Naik"))  ## Output: M Naik
print(generated_function("Nimit Singh"))  ## Output: N Singh


print(generated_function("John Singh"))  ### Output: J Singh
print(generated_function("Mayur Doe"))  ### Output: M Doe
print(generated_function("Nimit Naik"))  ### Output: N Naik

# TEST SCRIPTS APPENDED!

