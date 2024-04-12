# Start time: 2024-04-09 14:49:33.742936

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Summary for Input Column Data:

The input data consists of full names of individuals, each entry comprising a first name followed by a last name. These names appear to represent a diverse set of origins, indicating a multicultural dataset. Each entry is structured in a consistent format, with the first name and last name separated by a space. The dataset includes both single and multi-syllable names, suggesting variability in the length and complexity of the names. The names are presented in a standard capitalization format, with the first letter of each name capitalized, which is common in personal names across various cultures.

### Summary for Output Column Data:

The output data extracts and presents only the first name from each full name provided in the input data. This extraction process results in a dataset that consists solely of first names, maintaining the original capitalization and spelling. The output data retains the diversity and multicultural aspect of the input data, as it includes first names of various origins and structures. The transformation from the input to the output data involves removing the last name and any additional components of the full name, simplifying the dataset to focus exclusively on first names.

### Relationship Between Input and Output Data:

The relationship between the input and output data is characterized by a systematic extraction process, where the output is derived by isolating the first name from the full name provided in the input. This process demonstrates a one-to-one mapping from the full name to the first name, indicating a direct and consistent method of data transformation. The output data represents a subset of the information contained in the input data, specifically focusing on the component of the personal name that typically denotes the individual's given name. This transformation highlights the importance of first names in the dataset, potentially for applications or analyses where the specificity of individual identity is less critical than the recognition or categorization of individuals by their first names. The relationship underscores a simplification and focusing of the dataset from a more comprehensive personal identifier to a more general and widely applicable identifier., and input as ['Nancy FreeHafer'] output is Nancy, input as ['Andrew Cencici'] output is Andrew, input as ['Jan Kotas'] output is Jan, input as ['Mariya Sergienko'] output is Mariya, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(full_name):
    """
    Extracts and returns the first name from a given full name.
    
    Parameters:
    full_name (str): The full name of an individual, consisting of a first name followed by a last name.
    
    Returns:
    str: The first name extracted from the full name.
    """
    # Split the full name into parts and return the first part (first name)
    return full_name.split()[0]

# Test cases
print(generated_function('Nancy FreeHafer'))  # Expected output: Nancy
print(generated_function('Andrew Cencici'))  # Expected output: Andrew
print(generated_function('Jan Kotas'))       # Expected output: Jan
print(generated_function('Mariya Sergienko'))  # Expected output: Mariya
print(generated_function("Nancy FreeHafer"))  ## Output: Nancy
print(generated_function("Andrew Cencici"))  ## Output: Andrew
print(generated_function("Jan Kotas"))  ## Output: Jan
print(generated_function("Mariya Sergienko"))  ## Output: Mariya

# End time: 2024-04-09 14:49:40.926626
# Elapsed time in seconds: 7.18366107699876