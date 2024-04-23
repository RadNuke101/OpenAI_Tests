# Start time: 2024-04-09 17:48:11.336398

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input column consists of full names, each entry containing a combination of first, middle, and last names. These names are presented in a standard Western naming format, starting with the given name (commonly referred to as the first name), followed by middle names (which can be one or more), and ending with the surname (also known as the last name). The names are diverse, encompassing a range of potentially different cultural or ethnic backgrounds as indicated by the variety in the naming patterns. Each entry is structured as a single string, encapsulating the full name of an individual without any explicit separators (like commas) between the first, middle, and last names. The data is qualitative, focusing on the composition and structure of personal names.

### Output Column Summary:

The output column consists of the last names extracted from the full names provided in the input column. Each entry in the output column corresponds directly to the last name of the individual named in the input column. The output retains the original formatting and capitalization of the last names as they appeared in the input. This column simplifies the qualitative data from the input by isolating a specific component of the names, focusing solely on the surnames. The process of deriving the output from the input involves identifying and extracting the last word from each full name string, under the assumption that this last word represents the surname in the given naming convention.

### Relationship Between Input and Output:

The relationship between the input and output columns is a process of extraction and simplification, where the complex, multi-part names in the input are reduced to their simplest, most identifying component: the surname. This process assumes a consistent naming convention where the last word in the input string is the surname, which is a common pattern in many Western cultures but may not universally apply to all naming conventions globally. The transformation from input to output represents a focus shift from the full identity of an individual, as encapsulated by their complete name, to a more generic identifier that places emphasis on lineage or family connection, as represented by the surname. This operation highlights the surname as a key piece of qualitative data within the broader context of personal identification, simplifying the dataset while preserving a crucial element of personal identity., and input as ['Sarah Jane Jones'] output is Jones, input as ['Bob Jane Smithfield'] output is Smithfield, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(full_name):
    """
    Extracts the last name from a given full name string.

    Parameters:
    full_name (str): A string containing the full name of an individual, 
                     structured as first, middle (optional), and last names.

    Returns:
    str: The last name extracted from the full name.
    """
    # Split the full name into parts based on spaces
    name_parts = full_name.split()
    # The last name is assumed to be the last word in the full name
    last_name = name_parts[-1]
    return last_name

# Test cases
print(generated_function('Sarah Jane Jones'))  # Expected output: Jones
print(generated_function('Bob Jane Smithfield'))  # Expected output: Smithfield
print(generated_function("Sarah Jane Jones"))  ## Output: Jones
print(generated_function("Bob Jane Smithfield"))  ## Output: Smithfield

# End time: 2024-04-09 17:48:20.148986
# Elapsed time in seconds: 8.812350849999348


# APPEND TEST SCRIPTS...
print(generated_function("Sarah Jane Jones"))  ## Output: Jones
print(generated_function("Bob Jane Smithfield"))  ## Output: Smithfield


print(generated_function("Jones Jane Sarah"))  ### Output: Sarah
print(generated_function("Smithfield Jane Bob"))  ### Output: Bob

# TEST SCRIPTS APPENDED!

