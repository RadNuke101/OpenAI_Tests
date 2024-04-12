# Start time: 2024-04-05 16:38:18.288427

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return first letter of first word, followed by a space, and then the second word, and input as ['John Doe'] output is J Doe, input as ['Mayur Naik'] output is M Naik, input as ['Nimit Singh'] output is N Singh, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(full_name):
    """
    Takes a full name as input and returns the first letter of the first word,
    followed by a space, and then the second word.
    
    :param full_name: A string containing a first name and a last name.
    :return: A string with the first letter of the first name, a space, and the last name.
    """
    # Split the full name into a list of words
    name_parts = full_name.split()
    
    # Check if the name is properly split into at least two parts
    if len(name_parts) >= 2:
        # Construct the desired output format
        output = name_parts[0][0] + " " + name_parts[1]
    else:
        # If not, return an error message or handle accordingly
        output = "Invalid input"
    
    return output

# Test cases
print(generated_function('John Doe'))  # Expected output: J Doe
print(generated_function('Mayur Naik'))  # Expected output: M Naik
print(generated_function('Nimit Singh'))  # Expected output: N Singh
print(generated_function("John Doe"))  ## Output: J Doe
print(generated_function("Mayur Naik"))  ## Output: M Naik
print(generated_function("Nimit Singh"))  ## Output: N Singh

# End time: 2024-04-05 16:38:24.503730
# Elapsed time in seconds: 6.215959866000048