# Start time: 2024-04-05 17:13:19.384538

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return first letter of first word, followed by a space, and then the second word, and input as ['John Doe'] output is J Doe, input as ['Mayur Naik'] output is M Naik, input as ['Nimit Singh'] output is N Singh, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(full_name):
    """
    Takes a full name as input and returns the first letter of the first name,
    followed by a space, and then the second name.
    
    :param full_name: A string containing the first and last name.
    :return: A string with the first letter of the first name, a space, and the last name.
    """
    # Split the full name into first and last names
    parts = full_name.split()
    # Return the first letter of the first name, a space, and the last name
    return parts[0][0] + " " + parts[1]

# Test cases
print(generated_function('John Doe'))  # Expected output: J Doe
print(generated_function('Mayur Naik'))  # Expected output: M Naik
print(generated_function('Nimit Singh'))  # Expected output: N Singh
print(generated_function("John Doe"))  ## Output: J Doe
print(generated_function("Mayur Naik"))  ## Output: M Naik
print(generated_function("Nimit Singh"))  ## Output: N Singh

# End time: 2024-04-05 17:13:24.956369
# Elapsed time in seconds: 5.571672961000331


# APPEND TEST SCRIPTS...
print(generated_function("John Doe"))  ## Output: J Doe
print(generated_function("Mayur Naik"))  ## Output: M Naik
print(generated_function("Nimit Singh"))  ## Output: N Singh


print(generated_function("John Singh"))  ### Output: J Singh
print(generated_function("Mayur Doe"))  ### Output: M Doe
print(generated_function("Nimit Naik"))  ### Output: N Naik

# TEST SCRIPTS APPENDED!

