# Start time: 2024-04-09 18:34:51.025761

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input data consists of full names of individuals, each entry comprising a first name followed by a last name. These names appear to be of diverse ethnic origins, indicating a multicultural dataset. Each entry is structured in a consistent format, with the first name and last name separated by a space. The dataset does not include middle names or initials, focusing solely on the primary components of a person's name. The names are presented in a standard capitalization format, with the first letter of each name capitalized, suggesting a formal or official listing of names as might be found in a database or registry.

### Output Column Summary:

The output data extracts and presents the last name from each full name provided in the input column. This transformation retains the original capitalization and spelling of the last names, ensuring that the integrity of the names is maintained. The output focuses on isolating the family name component of each individual's full name, effectively simplifying the data from a complete identity to a categorical identifier that could be used for sorting, grouping, or indexing purposes.

### Relationship Between Input and Output:

The relationship between the input and output data is a process of extraction and simplification, where the output isolates a specific component (the last name) from a more complex structure (the full name) provided in the input. This transformation is consistent across the dataset, applying the same method of extraction to each entry without exception. The process highlights the last names as a significant identifier within the dataset, potentially for purposes of analysis, organization, or identification that prioritizes family lineage or grouping individuals by their last names. The methodology applied does not alter the original data (i.e., the spelling or capitalization of the last names) but rather filters out the first name to focus on the surname as the primary data point of interest. This relationship underscores a common practice in data processing where specific attributes are isolated from a larger dataset to facilitate targeted analysis or operations., and input as ['Nancy FreeHafer'] output is FreeHafer, input as ['Andrew Cencici'] output is Cencici, input as ['Jan Kotas'] output is Kotas, input as ['Mariya Sergienko'] output is Sergienko, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(full_name):
    """
    Extracts and returns the last name from a full name input.
    
    Parameters:
    full_name (str): A string containing a first name and a last name separated by a space.
    
    Returns:
    str: The last name extracted from the full name.
    """
    # Split the full name into parts and return the last part (last name)
    return full_name.split(" ")[-1]

# Test cases
print(generated_function('Nancy FreeHafer'))  # Expected output: FreeHafer
print(generated_function('Andrew Cencici'))  # Expected output: Cencici
print(generated_function('Jan Kotas'))  # Expected output: Kotas
print(generated_function('Mariya Sergienko'))  # Expected output: Sergienko
print(generated_function("Nancy FreeHafer"))  ## Output: FreeHafer
print(generated_function("Andrew Cencici"))  ## Output: Cencici
print(generated_function("Jan Kotas"))  ## Output: Kotas
print(generated_function("Mariya Sergienko"))  ## Output: Sergienko

# End time: 2024-04-09 18:34:58.192869
# Elapsed time in seconds: 7.166896093000105