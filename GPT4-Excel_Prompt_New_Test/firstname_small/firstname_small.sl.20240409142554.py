# Start time: 2024-04-09 15:13:44.903462

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Summary for Input Column Data:

The input data consists of full names of individuals, each entry comprising a first name followed by a last name. These names appear to be of diverse ethnic origins, indicating a multicultural dataset. Each entry is structured in a consistent format, with the first name and last name separated by a space, and each name starts with a capital letter, adhering to standard conventions of written English names. The dataset includes both single and multi-syllable names, suggesting a variety of linguistic backgrounds. The names are presented as a single string within an array, which could imply that the data is intended for processing in a programming or data analysis context where each entry is treated as an individual element.

### Summary for Output Column Data:

The output data consists solely of first names extracted from the full names provided in the input data. Each output retains the capitalization from the input, indicating that the transformation process respects the original case formatting. The output data, like the input, showcases a diversity of names, but with the simplification of removing last names, it focuses on the individual identity aspect of the data. This reduction to first names could serve purposes such as personalization or identification in contexts where the full name is unnecessary or privacy is a concern.

### Relationship Between Input and Output:

The relationship between the input and output data is a process of extraction and simplification, where the output is derived by isolating the first name from each full name in the input. This process involves identifying the first word in each input string (assuming the first word is the first name) and discarding the subsequent text (assumed to be the last name). The consistent structure of the input data, with names following the "First Last" format, facilitates this extraction. The transformation from input to output suggests an application or analysis that requires only the personal identifier (the first name) without the additional context or specificity provided by the last name. This could be useful in scenarios where the focus is on personal interaction or where data minimization principles are applied., and input as ['Nancy FreeHafer'] output is Nancy, input as ['Andrew Cencici'] output is Andrew, input as ['Jan Kotas'] output is Jan, input as ['Mariya Sergienko'] output is Mariya, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(full_name):
    """
    Extracts and returns the first name from a given full name.
    
    Parameters:
    full_name (str): A string containing the full name of an individual.
    
    Returns:
    str: The first name extracted from the full name.
    """
    # Split the full name into parts and return the first part (first name)
    return full_name.split()[0]

# Test cases
print(generated_function('Nancy FreeHafer'))  # Expected output: Nancy
print(generated_function('Andrew Cencici'))  # Expected output: Andrew
print(generated_function('Jan Kotas'))  # Expected output: Jan
print(generated_function('Mariya Sergienko'))  # Expected output: Mariya
print(generated_function("Nancy FreeHafer"))  ## Output: Nancy
print(generated_function("Andrew Cencici"))  ## Output: Andrew
print(generated_function("Jan Kotas"))  ## Output: Jan
print(generated_function("Mariya Sergienko"))  ## Output: Mariya

# End time: 2024-04-09 15:13:53.110497
# Elapsed time in seconds: 8.206904135999139


# APPEND TEST SCRIPTS...
print(generated_function("Nancy FreeHafer"))  ## Output: Nancy
print(generated_function("Andrew Cencici"))  ## Output: Andrew
print(generated_function("Jan Kotas"))  ## Output: Jan
print(generated_function("Mariya Sergienko"))  ## Output: Mariya


print(generated_function("Jackson Turner"))  ### Output: Jackson
print(generated_function("Caleb Mitchell"))  ### Output: Caleb
print(generated_function("Benjamin Hayes"))  ### Output: Benjamin
print(generated_function("Grace Harrison"))  ### Output: Grace
print(generated_function("Mason Thompson"))  ### Output: Mason
print(generated_function("Lily Anderson"))  ### Output: Lily
print(generated_function("Wyatt Davis"))  ### Output: Wyatt
print(generated_function("Olivia Parker"))  ### Output: Olivia
print(generated_function("Emma Reynolds"))  ### Output: Emma

# TEST SCRIPTS APPENDED!

