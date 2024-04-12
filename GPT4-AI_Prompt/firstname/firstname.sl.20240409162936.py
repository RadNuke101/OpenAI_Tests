# Start time: 2024-04-09 16:48:08.065541

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input column consists of full names of individuals, each entry formatted as a single string. These names are composed of two parts: the first name and the last name, separated by a space. The dataset includes a variety of names, suggesting a diverse set of individuals. The names appear to be of various ethnic origins, indicating a multicultural dataset. Each entry is unique, and there are no duplicates or numerical values included in the input data. The names are presented in a standard format, with the first name followed by the last name, without any titles or middle names included.

### Output Column Summary:

The output column contains only the first names extracted from the full names provided in the input column. Each entry in the output corresponds directly to the first part of the full name from the input, effectively isolating the first name from the last name. The output retains the original formatting of the first names, including capitalization. This column simplifies the input data by focusing solely on the first names, removing any information related to the last names. The diversity in the first names is preserved, reflecting the variety present in the input data.

### Relationship Between Input and Output:

The relationship between the input and output columns is straightforward: the output is derived directly from the input by extracting the first name from each full name provided. This process involves identifying the first space character in the input string and isolating the substring that precedes it, which corresponds to the first name. The transformation from input to output simplifies the data by removing the last names, focusing solely on the individuals' first names. This operation preserves the uniqueness and diversity of the names while streamlining the information to include only the first component of each full name. The relationship highlights a method of data reduction and simplification, where detailed personal information (full names) is condensed into a more general form (first names), facilitating analyses or operations that require less detailed personal identifiers., and input as ['Nancy FreeHafer'] output is Nancy, input as ['Andrew Cencici'] output is Andrew, input as ['Jan Kotas'] output is Jan, input as ['Mariya Sergienko'] output is Mariya, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(full_name):
    """
    Extracts the first name from a full name string.

    Parameters:
    full_name (str): A string containing a first name and a last name separated by a space.

    Returns:
    str: The first name extracted from the full name.
    """
    # Split the full name by space and return the first element
    return full_name.split(' ')[0]

# Test cases
print(generated_function('Nancy FreeHafer'))  # Expected output: Nancy
print(generated_function('Andrew Cencici'))  # Expected output: Andrew
print(generated_function('Jan Kotas'))  # Expected output: Jan
print(generated_function('Mariya Sergienko'))  # Expected output: Mariya
print(generated_function("Nancy FreeHafer"))  ## Output: Nancy
print(generated_function("Andrew Cencici"))  ## Output: Andrew
print(generated_function("Jan Kotas"))  ## Output: Jan
print(generated_function("Mariya Sergienko"))  ## Output: Mariya

# End time: 2024-04-09 16:48:13.047184
# Elapsed time in seconds: 4.981574526000259