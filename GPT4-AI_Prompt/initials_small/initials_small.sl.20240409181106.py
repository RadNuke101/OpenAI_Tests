# Start time: 2024-04-09 19:02:50.460065

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Summary of Input Column Data:

The input column consists of full names of individuals, each entry containing a first name followed by a last name. These names are diverse in origin, indicating a variety of cultural backgrounds. Each entry is structured in a consistent format, with the first name followed by the last name, separated by a space. The names vary in length and complexity, reflecting a wide range of naming conventions. The data is qualitative, representing personal identifiers without implying any quantitative relationships or hierarchies among the entries.

### Summary of Output Column Data:

The output column presents initials derived from the corresponding full names in the input column. Each entry consists of two letters, the first initial of the first name and the first initial of the last name, separated by a period. This format standardizes the representation of the diverse names in the input column into a concise, uniform format. The output is qualitative, serving as a simplified identifier that retains a direct, albeit abstracted, link to the original name.

### Relationship Between Input and Output:

The relationship between the input and output columns is a transformational one, where the complex, variable-length, and culturally diverse full names are systematically reduced to a standardized, concise format of initials. This transformation involves extracting the first letter of the first name and the first letter of the last name from each entry in the input column and then concatenating these letters with a period in between. The process preserves a unique identifier for each individual, albeit in a much-reduced form, facilitating easier reference or categorization without the detail and cultural specificity of the full names. This method of abbreviation is common in various contexts, including professional, academic, and bureaucratic settings, where space or clarity necessitates brevity., and input as ['Nancy FreeHafer'] output is N.F., input as ['Andrew Cencici'] output is A.C., input as ['Jan Kotas'] output is J.K., input as ['Mariya Sergienko'] output is M.S., , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(full_name):
    """
    This function takes a full name as input and returns the initials of the first and last name,
    separated by a period.
    
    :param full_name: A string containing a first name and a last name separated by a space.
    :return: A string containing the initials of the first and last name separated by a period.
    """
    # Split the full name into first name and last name
    first_name, last_name = full_name.split()
    # Extract the first letter of the first name and the first letter of the last name
    initials = first_name[0] + "." + last_name[0]
    return initials.upper()

# Test cases
print(generated_function('Nancy FreeHafer'))  # Expected output: N.F.
print(generated_function('Andrew Cencici'))  # Expected output: A.C.
print(generated_function('Jan Kotas'))  # Expected output: J.K.
print(generated_function('Mariya Sergienko'))  # Expected output: M.S.
print(generated_function("Nancy FreeHafer"))  ## Output: N.F.
print(generated_function("Andrew Cencici"))  ## Output: A.C.
print(generated_function("Jan Kotas"))  ## Output: J.K.
print(generated_function("Mariya Sergienko"))  ## Output: M.S.

# End time: 2024-04-09 19:03:00.091478
# Elapsed time in seconds: 9.631228882000869