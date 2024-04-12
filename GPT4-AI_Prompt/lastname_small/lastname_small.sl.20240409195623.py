# Start time: 2024-04-09 20:22:06.667821

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input column consists of full names of individuals, each entry formatted as a single string. These names appear to follow a conventional Western naming pattern, where each entry is composed of a first name followed by a last name, separated by a space. The dataset includes a variety of names that suggest a diverse set of origins or backgrounds, indicating no specific geographical or cultural concentration. Each entry is unique, with no repetitions of the same name, highlighting a sample of individuals rather than groups or categories.

### Output Column Summary:

The output column contains the last names extracted from the full names provided in the input column. Each output is a single word, representing the family name or surname of the individual mentioned in the corresponding input entry. This column simplifies the information from the input by isolating the last component of each full name, effectively focusing on the part of the name that, in many cultures, is passed down through generations and can carry implications of lineage, heritage, and familial connections.

### Relationship Summary:

The relationship between the input and output columns is straightforward and systematic: the output is derived directly from the input by extracting the last name from each full name provided. This process involves identifying the space that separates the first name from the last name in the input and then isolating the latter part. The transformation from input to output simplifies the data from a more complex form (full names) to a simpler, more uniform format (last names only), making it easier to analyze patterns related to family names, such as cultural or geographical origins, without the additional variable of first names. This method of data simplification could be particularly useful in contexts where the specific identity of individuals is less relevant than the broader patterns or categories their last names might represent., and input as ['Nancy FreeHafer'] output is FreeHafer, input as ['Andrew Cencici'] output is Cencici, input as ['Jan Kotas'] output is Kotas, input as ['Mariya Sergienko'] output is Sergienko, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(full_name):
    """
    Extracts and returns the last name from a given full name.
    
    Parameters:
    full_name (str): A string containing the first name and last name separated by a space.
    
    Returns:
    str: The last name extracted from the full name.
    """
    # Split the full name into parts using space as the separator
    name_parts = full_name.split(' ')
    # The last name is assumed to be the last element in the list
    last_name = name_parts[-1]
    return last_name

# Test cases
print(generated_function('Nancy FreeHafer'))  # Expected output: FreeHafer
print(generated_function('Andrew Cencici'))  # Expected output: Cencici
print(generated_function('Jan Kotas'))  # Expected output: Kotas
print(generated_function('Mariya Sergienko'))  # Expected output: Sergienko
print(generated_function("Nancy FreeHafer"))  ## Output: FreeHafer
print(generated_function("Andrew Cencici"))  ## Output: Cencici
print(generated_function("Jan Kotas"))  ## Output: Kotas
print(generated_function("Mariya Sergienko"))  ## Output: Sergienko

# End time: 2024-04-09 20:22:16.056018
# Elapsed time in seconds: 9.387992649000807