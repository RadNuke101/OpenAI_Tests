# Start time: 2024-04-09 18:47:47.584364

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input column consists of full names of individuals, each entry formatted as a string containing a first name followed by a last name, separated by a space. Each name is unique and represents a distinct individual. The first names and last names vary in length and cultural origin, indicating a diverse dataset. The input data is qualitative, focusing on the textual representation of personal names.

### Output Column Summary:

The output column simplifies the input names into a more concise format. Each output entry retains the initial of the first name followed by the full last name, separated by a space. This transformation reduces the length of each entry while maintaining a level of uniqueness and personal identification. The output is also qualitative, representing a modified version of the input names that emphasizes brevity and the preservation of identifiable information.

### Relationship Summary:

The transformation from the input to the output column demonstrates a systematic process of abbreviation. The relationship between the input and output data is characterized by the retention of the initial letter from each individual's first name and the complete last name, discarding the rest of the first name. This process suggests a focus on maintaining essential identity markers (the initial of the first name and the entirety of the last name) while streamlining the data for scenarios where full names might be unnecessary or where space is limited. The method applied is consistent across all entries, indicating a rule-based approach to generating the output from the input data. This relationship highlights a balance between brevity and the need to preserve identifiable information within a dataset., and input as ['John Doe'] output is J Doe, input as ['Mayur Naik'] output is M Naik, input as ['Nimit Singh'] output is N Singh, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(full_name):
    """
    This function takes a full name as input and returns a simplified version of the name.
    The simplified version retains the initial of the first name followed by the full last name,
    separated by a space.
    
    :param full_name: A string containing a first name and a last name separated by a space.
    :return: A string with the initial of the first name followed by the full last name.
    """
    # Split the full name into first name and last name
    first_name, last_name = full_name.split()
    # Create the simplified name format
    simplified_name = first_name[0] + " " + last_name
    return simplified_name

# Test cases
print(generated_function('John Doe'))  # Expected output: J Doe
print(generated_function('Mayur Naik'))  # Expected output: M Naik
print(generated_function('Nimit Singh'))  # Expected output: N Singh
print(generated_function("John Doe"))  ## Output: J Doe
print(generated_function("Mayur Naik"))  ## Output: M Naik
print(generated_function("Nimit Singh"))  ## Output: N Singh

# End time: 2024-04-09 18:47:54.446171
# Elapsed time in seconds: 6.86170834099903