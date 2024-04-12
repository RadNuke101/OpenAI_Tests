# Start time: 2024-04-09 12:49:17.528128

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Summary for Input Column Data:

The input data consists of full names of individuals, each entry comprising a first name followed by a last name. These names appear to be of diverse ethnic origins, indicating a multicultural dataset. The structure is consistent across all entries, with each name separated by a space. The first names vary in length and cultural background, including names like Nancy, Andrew, Jan, and Mariya, suggesting a wide range of identities. The last names, such as FreeHafer, Cencici, Kotas, and Sergienko, also show a variety of origins, potentially indicating a global dataset or a dataset from a multicultural region.

### Summary for Output Column Data:

The output data consists solely of the last names extracted from the full names provided in the input data. These last names, including FreeHafer, Cencici, Kotas, and Sergienko, retain the diversity seen in the input data, reflecting a range of cultural backgrounds. The output data is structured uniformly, with each entry containing a single word without spaces, representing the last name of the individuals from the input data.

### Relationship Summary:

The relationship between the input and output data is a process of extraction, where the output is derived by isolating the last name from each full name provided in the input. This process involves identifying and separating the last name from the first name within each full name entry. The transformation from input to output demonstrates a filtering or reduction operation, focusing on retaining only the last name component of the full names. This operation suggests an interest in or relevance of the last names in isolation, possibly for purposes where the specific identity or cultural background signified by the last name is of primary importance. The consistent structure across the input and output data indicates a systematic approach to data handling, aimed at simplifying or focusing the dataset for further analysis or application, where only the last names are required., and input as ['Nancy FreeHafer'] output is FreeHafer, input as ['Andrew Cencici'] output is Cencici, input as ['Jan Kotas'] output is Kotas, input as ['Mariya Sergienko'] output is Sergienko, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(full_name):
    """
    Extracts and returns the last name from a given full name.
    
    Parameters:
    full_name (str): A string containing a first name and a last name separated by a space.
    
    Returns:
    str: The last name extracted from the full name.
    """
    # Split the full name into parts assuming the last name is the last part
    name_parts = full_name.split(' ')
    # Return the last part which is assumed to be the last name
    return name_parts[-1]

# Test cases
print(generated_function('Nancy FreeHafer'))  # Expected output: FreeHafer
print(generated_function('Andrew Cencici'))  # Expected output: Cencici
print(generated_function('Jan Kotas'))  # Expected output: Kotas
print(generated_function('Mariya Sergienko'))  # Expected output: Sergienko
print(generated_function("Nancy FreeHafer"))  ## Output: FreeHafer
print(generated_function("Andrew Cencici"))  ## Output: Cencici
print(generated_function("Jan Kotas"))  ## Output: Kotas
print(generated_function("Mariya Sergienko"))  ## Output: Sergienko

# End time: 2024-04-09 12:49:27.748853
# Elapsed time in seconds: 10.220530080000117