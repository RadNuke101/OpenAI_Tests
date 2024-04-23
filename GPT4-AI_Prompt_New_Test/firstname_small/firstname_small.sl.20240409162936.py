# Start time: 2024-04-09 17:09:15.839879

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Summary for Input Column Data:

The input column consists of full names of individuals, each entry formatted as a single string. These names are structured in a traditional Western naming convention, where each entry starts with a given name (commonly referred to as a "first name") followed by a family name (often called a "surname" or "last name"). The dataset includes a variety of names that suggest a diversity in terms of cultural or ethnic origins. The names are presented in a consistent format, with the given name and family name separated by a space. There is no indication of titles, middle names, or initials, keeping the data straightforward and focused solely on primary given and family names.

### Summary for Output Column Data:

The output column data consists solely of given names extracted from the full names provided in the input column. Each entry in the output column corresponds directly to the first part of each full name from the input column, effectively isolating the given name from the full name. The output data retains the original formatting of the given names, including capitalization, but does not include any family names, titles, or additional identifiers. This simplification process transforms the full name data into a list of given names, making it easier to analyze or utilize the data in contexts where only the individual's given name is relevant.

### Relationship Summary between Input and Output Columns:

The relationship between the input and output columns is characterized by a systematic extraction process, where the output is derived by isolating the first segment (the given name) of each full name provided in the input. This process suggests a consistent method of data simplification or reduction, where the primary objective is to focus on the individual's given name for purposes that may include personalization, identification in less formal contexts, or any scenario where the family name is deemed unnecessary. The transformation from full names to given names indicates a clear, direct relationship that prioritizes the initial component of each input data entry, demonstrating a straightforward method of data processing aimed at extracting specific, relevant information from a more complex dataset., and input as ['Nancy FreeHafer'] output is Nancy, input as ['Andrew Cencici'] output is Andrew, input as ['Jan Kotas'] output is Jan, input as ['Mariya Sergienko'] output is Mariya, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(full_name):
    """
    Extracts the given name from a full name string.

    Parameters:
    full_name (str): A string containing a full name in the format "GivenName FamilyName".

    Returns:
    str: The extracted given name from the full name.
    """
    # Split the full name into parts and return the first part (given name)
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

# End time: 2024-04-09 17:09:22.393334
# Elapsed time in seconds: 6.553335567001341


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

