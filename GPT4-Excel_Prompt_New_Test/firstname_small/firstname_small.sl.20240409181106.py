# Start time: 2024-04-09 18:48:28.042498

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input column consists of full names of individuals, each entry formatted as a single string. These names are composed of at least two parts: a given name (or first name) and a surname (or last name), separated by a space. The dataset includes a variety of names, suggesting a diverse set of individuals. The names appear to be of various ethnic origins, indicating a multicultural dataset. Each entry is unique, and the format is consistent across the dataset.

### Output Column Summary:

The output column contains only the given names (or first names) extracted from the full names provided in the input column. Each output is a single word, representing the first part of the corresponding input. The output retains the original capitalization found in the input, suggesting a direct extraction without alteration of the case. This column simplifies the input data by focusing solely on the given names, removing any surname information.

### Relationship Summary:

The relationship between the input and output columns is a straightforward extraction process, where the output is derived by isolating the first segment (given name) of the input (full name). This process involves parsing each full name string in the input column, identifying the first name based on its position (before the first space), and then copying that segment into the output column. The transformation from input to output simplifies the data by removing the surnames, focusing solely on the individuals' given names. This relationship indicates a methodical approach to distilling a specific type of information (given names) from a more complex dataset (full names), which could be useful for tasks requiring personalization or identification without the need for full identity disclosure., and input as ['Nancy FreeHafer'] output is Nancy, input as ['Andrew Cencici'] output is Andrew, input as ['Jan Kotas'] output is Jan, input as ['Mariya Sergienko'] output is Mariya, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(full_name):
    """
    Extracts the given name from a full name.

    Parameters:
    full_name (str): A string containing the full name of an individual, 
                     formatted as 'GivenName Surname'.

    Returns:
    str: The given name extracted from the full name.
    """
    # Split the full name by space and return the first element (given name)
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

# End time: 2024-04-09 18:48:34.894780
# Elapsed time in seconds: 6.852182021997578


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

