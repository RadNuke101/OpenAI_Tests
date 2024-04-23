# Start time: 2024-04-09 21:20:18.440548

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Summary of Input Column Data:

The input column consists of full names, each entry being a single string that includes one or more given names followed by a surname. These names appear to follow a common naming convention in many English-speaking countries, where individuals may have a first name, possibly one or more middle names, and a last name that represents the family name or surname. The names provided in the input are diverse in terms of the number of components they contain, indicating variability in the length and structure of the names. The input data is qualitative, representing categorical, non-numeric information specific to individual identities.

### Summary of Output Column Data:

The output column data consists of single-word strings, each representing a surname extracted from the corresponding full name in the input column. These surnames are the last word in each full name provided in the input, following the convention that the surname appears at the end of a person's full name in many cultures. The output data retains the qualitative nature of the input, focusing specifically on the component of the full name that denotes family or lineage.

### Summary of the Relationship Between Input and Output:

The relationship between the input and output data is characterized by a process of extraction, where the output is derived by identifying and isolating the last word from each full name in the input column. This process assumes a naming convention where the surname or family name is positioned as the final word in a person's full name. The transformation from input to output involves reducing the multi-component full name to its singular component that signifies familial or ancestral identity. This relationship underscores a focused interest in the lineage or family name aspect of personal identity, as represented in the dataset., and input as ['Sarah Jane Jones'] output is Jones, input as ['Bob Jane Smithfield'] output is Smithfield, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(full_name):
    """
    Extracts and returns the surname from a given full name.
    
    Parameters:
    full_name (str): A string representing a person's full name, 
                     following the format of one or more given names 
                     followed by a surname.
    
    Returns:
    str: The extracted surname from the full name.
    """
    # Split the full name into a list of names
    name_parts = full_name.split()
    # The surname is the last element in the list
    surname = name_parts[-1]
    return surname

# Test cases
print(generated_function('Sarah Jane Jones'))  # Expected output: Jones
print(generated_function('Bob Jane Smithfield'))  # Expected output: Smithfield
print(generated_function("Sarah Jane Jones"))  ## Output: Jones
print(generated_function("Bob Jane Smithfield"))  ## Output: Smithfield

# End time: 2024-04-09 21:20:24.695212
# Elapsed time in seconds: 6.254493056003412


# APPEND TEST SCRIPTS...
print(generated_function("Sarah Jane Jones"))  ## Output: Jones
print(generated_function("Bob Jane Smithfield"))  ## Output: Smithfield


print(generated_function("Jones Jane Sarah"))  ### Output: Sarah
print(generated_function("Smithfield Jane Bob"))  ### Output: Bob

# TEST SCRIPTS APPENDED!

