# Start time: 2024-04-09 16:00:26.196940

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input data consists of full names, each entry containing a combination of first, middle (optional), and last names. These names are structured in a conventional Western naming format, where the first name appears first, followed by the middle name (if any), and the last name appears at the end. The names are presented as a single string within an array for each entry. The dataset includes names with varying lengths, indicating a mix of names with and without middle names or potentially multiple middle names. The names are diverse, suggesting a wide range of backgrounds and cultures. However, they all adhere to the format of being presented in a single, unbroken string, encapsulating the full name of an individual without any explicit separators between first, middle, and last names other than spaces.

### Output Column Summary:

The output data extracts and presents the last name from each full name provided in the input column. Each output is a single string that represents the last name of the individual from the corresponding input entry. The output is structured to isolate and identify the last component of the name from the input, assuming that the last word in the input string is the last name. This process simplifies the full name to its family name component, providing a concise identifier for each entry.

### Relationship Summary:

The relationship between the input and output data is a process of extraction and simplification, where the output isolates the last name from the full name provided in the input. This transformation assumes a consistent naming convention where the last word in the input string is the individual's last name. The process disregards any first names or middle names, focusing solely on identifying and extracting the family name. This operation serves to distill the input data to a key component of personal identification, the last name, which can be used for sorting, indexing, or other purposes where a concise identifier is preferable. The methodology relies on the structural consistency of the input data, where the last name is always positioned at the end of the string, following any first or middle names., and input as ['Sarah Jane Jones'] output is Jones, input as ['Bob Jane Smithfield'] output is Smithfield, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(full_name):
    """
    Extracts and returns the last name from a full name string.
    
    Parameters:
    full_name (str): A string containing the full name of an individual.
    
    Returns:
    str: The last name extracted from the full name.
    """
    # Split the full name into parts based on spaces
    name_parts = full_name.split()
    # The last name is assumed to be the last element in the list
    last_name = name_parts[-1]
    return last_name

# Test cases
print(generated_function('Sarah Jane Jones'))  # Expected output: Jones
print(generated_function('Bob Jane Smithfield'))  # Expected output: Smithfield
print(generated_function("Sarah Jane Jones"))  ## Output: Jones
print(generated_function("Bob Jane Smithfield"))  ## Output: Smithfield

# End time: 2024-04-09 16:00:33.695620
# Elapsed time in seconds: 7.498487344999376


# APPEND TEST SCRIPTS...
print(generated_function("Sarah Jane Jones"))  ## Output: Jones
print(generated_function("Bob Jane Smithfield"))  ## Output: Smithfield


print(generated_function("Jones Jane Sarah"))  ### Output: Sarah
print(generated_function("Smithfield Jane Bob"))  ### Output: Bob

# TEST SCRIPTS APPENDED!

