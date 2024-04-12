# Start time: 2024-04-09 20:52:42.315487

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input data consists of full names of individuals, each entry comprising primarily of two parts: a first name and a last name. These names are culturally diverse, indicating a variety of ethnic backgrounds. Each name is structured in a conventional Western format, where the first name precedes the last name, separated by a space. The names are presented in a standard case, with the first letter of each name capitalized, which is typical for proper nouns in English. The input data is qualitative, representing personal identifiers rather than numerical values or measurable quantities.

### Output Column Summary:

The output data simplifies the input names into initials, maintaining the qualitative nature but reducing the detail to a minimal form. Each output is a pair of letters followed by periods (e.g., "N.F."), representing the first letters of the first and last names from the input data. These initials are also separated by a period, maintaining a consistent format across all entries. The output preserves the capitalization of the input, emphasizing the proper noun aspect of the names. This transformation from full names to initials abstracts the personal identity to a less identifiable form, focusing on the uniqueness of the combination of the starting letters of each name.

### Relationship Between Input and Output:

The relationship between the input and output data is a process of abbreviation, where the full names are condensed into their respective initials. This process retains the first letter of each name component (first and last name) and discards the rest of the characters. The output serves as a compact representation of the input, maintaining the distinctiveness of each entry through the unique combinations of initials. This method of abbreviation is commonly used for creating initials or acronyms, making the data easier to reference or use in contexts where space or simplicity is preferred. The transformation process is systematic and applies uniformly across all entries, indicating a straightforward, rule-based relationship between the input and output data., and input as ['Nancy FreeHafer'] output is N.F., input as ['Andrew Cencici'] output is A.C., input as ['Jan Kotas'] output is J.K., input as ['Mariya Sergienko'] output is M.S., , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(full_name):
    """
    This function takes a full name as input and returns the initials of the first and last name.
    
    Parameters:
    full_name (str): The full name of an individual, consisting of a first name and a last name.
    
    Returns:
    str: The initials of the first and last name, separated by a period and followed by a period.
    """
    # Split the full name into first name and last name based on space
    parts = full_name.split()
    # Extract the first letter of the first name and the last name, capitalize them, and format as initials
    initials = f"{parts[0][0]}.{parts[1][0]}."
    return initials

# Test cases
print(generated_function('Nancy FreeHafer'))  # Expected output: N.F.
print(generated_function('Andrew Cencici'))  # Expected output: A.C.
print(generated_function('Jan Kotas'))  # Expected output: J.K.
print(generated_function('Mariya Sergienko'))  # Expected output: M.S.
print(generated_function("Nancy FreeHafer"))  ## Output: N.F.
print(generated_function("Andrew Cencici"))  ## Output: A.C.
print(generated_function("Jan Kotas"))  ## Output: J.K.
print(generated_function("Mariya Sergienko"))  ## Output: M.S.

# End time: 2024-04-09 20:52:49.792073
# Elapsed time in seconds: 7.4763658459996805