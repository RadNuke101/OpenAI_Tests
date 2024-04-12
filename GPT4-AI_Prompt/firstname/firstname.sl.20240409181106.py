# Start time: 2024-04-09 18:29:30.100578

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input column consists of full names of individuals, each entry formatted as a single string. These names are composed of two main parts: the first name and the last name, separated by a space. The dataset includes a variety of names, indicating a diverse set of individuals. The names appear to be of various ethnic origins, suggesting a multicultural dataset. Each entry is unique, and there is no indication of duplication or variation in the formatting (e.g., inclusion of middle names or initials). The dataset provides a simple, straightforward structure for identifying individuals by their full names.

### Output Column Summary:

The output column contains only the first names extracted from the full names provided in the input column. Each entry in the output corresponds directly to the first part of the string (the first name) from the input column, before the space that separates the first name from the last name. This column simplifies the identification of individuals by their first names, removing the specificity and diversity of the last names. The output maintains the same order as the input, ensuring a one-to-one relationship between the input and output entries.

### Relationship Between Input and Output:

The relationship between the input and output columns is characterized by a transformation process that extracts the first name from each full name in the input column. This process involves identifying the first space in each input string as the delimiter between the first and last names and then selecting the substring that precedes this space. The transformation maintains the original order and count of entries, ensuring that each output name corresponds directly to the input name from which it was derived. This relationship highlights a focus on simplifying the identification of individuals by their first names, possibly for contexts where the specificity of a full name is unnecessary or where the familiarity of using a first name is preferred. The process respects the diversity of the input data while streamlining it for applications that require less formal identification., and input as ['Nancy FreeHafer'] output is Nancy, input as ['Andrew Cencici'] output is Andrew, input as ['Jan Kotas'] output is Jan, input as ['Mariya Sergienko'] output is Mariya, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(full_name):
    """
    Extracts the first name from a full name string.

    Parameters:
    full_name (str): A string containing a first name and a last name separated by a space.

    Returns:
    str: The first name extracted from the full name.
    """
    # Split the full name by space and return the first element (first name)
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

# End time: 2024-04-09 18:29:35.938443
# Elapsed time in seconds: 5.83769228500023