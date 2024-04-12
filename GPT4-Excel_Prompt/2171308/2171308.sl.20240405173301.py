# Start time: 2024-04-05 17:47:04.322043

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return first letter of first word, followed by a space, and then the second word, and input as ['John Doe'] output is J Doe, input as ['Mayur Naik'] output is M Naik, input as ['Nimit Singh'] output is N Singh, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(full_name):
    """
    This function takes a full name as input, extracts the first letter of the first word,
    and combines it with the second word, separated by a space.
    
    :param full_name: A string containing at least two words.
    :return: A string with the first letter of the first word, a space, and the second word.
    """
    # Split the full name into words
    words = full_name.split()
    
    # Extract the first letter of the first word and the second word
    result = f"{words[0][0]} {words[1]}"
    
    return result

# Test cases
print(generated_function('John Doe'))  # Expected output: J Doe
print(generated_function('Mayur Naik'))  # Expected output: M Naik
print(generated_function('Nimit Singh'))  # Expected output: N Singh
print(generated_function("John Doe"))  ## Output: J Doe
print(generated_function("Mayur Naik"))  ## Output: M Naik
print(generated_function("Nimit Singh"))  ## Output: N Singh

# End time: 2024-04-05 17:47:11.196512
# Elapsed time in seconds: 6.874284114000147