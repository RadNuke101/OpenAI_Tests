# Start time: 2024-04-09 16:53:51.668266

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input column consists of full names of individuals, each entry formatted as a single string. These names are structured in the traditional Western naming convention, where each entry is composed of a given name (often referred to as a "first name") followed by a family name (commonly called a "last name"). The names appear to be diverse, suggesting a variety of cultural backgrounds. Each name is separated by a space, indicating a clear distinction between the given name and the family name. The input data does not include any titles, middle names, or initials, focusing solely on the primary components of a person's name.

### Output Column Summary:

The output column contains the family names extracted from the full names provided in the input column. Each entry in the output corresponds directly to the second part of the full name from the input, signifying the extraction of the family name component. This column simplifies the identity of each individual to their family name, disregarding the given names. The output maintains the original formatting and capitalization of the family names as they appeared in the input.

### Relationship Summary:

The relationship between the input and output columns is a process of extraction and simplification, where the output is derived by isolating the family name from each full name in the input. This process involves identifying the space that separates the given name from the family name in the input and then selecting the portion of the string that follows. The transformation from input to output discards the given names, focusing solely on the family names, which are of primary interest in this context. This method assumes a consistent naming convention across the input data, where the family name follows the given name, separated by a space. The output serves to highlight familial or ancestral connections by emphasizing the family names, which can be particularly useful in contexts where such distinctions are relevant., and input as ['Nancy FreeHafer'] output is FreeHafer, input as ['Andrew Cencici'] output is Cencici, input as ['Jan Kotas'] output is Kotas, input as ['Mariya Sergienko'] output is Sergienko, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(full_name):
    """
    Extracts and returns the family name from a given full name.
    
    Parameters:
    full_name (str): A string containing a full name in the format "GivenName FamilyName".
    
    Returns:
    str: The extracted family name.
    """
    # Split the full name into parts and return the last part (family name)
    return full_name.split()[-1]

# Test cases
print(generated_function('Nancy FreeHafer'))  # Expected output: FreeHafer
print(generated_function('Andrew Cencici'))  # Expected output: Cencici
print(generated_function('Jan Kotas'))  # Expected output: Kotas
print(generated_function('Mariya Sergienko'))  # Expected output: Sergienko
print(generated_function("Nancy FreeHafer"))  ## Output: FreeHafer
print(generated_function("Andrew Cencici"))  ## Output: Cencici
print(generated_function("Jan Kotas"))  ## Output: Kotas
print(generated_function("Mariya Sergienko"))  ## Output: Sergienko

# End time: 2024-04-09 16:53:57.406324
# Elapsed time in seconds: 5.737970997000957