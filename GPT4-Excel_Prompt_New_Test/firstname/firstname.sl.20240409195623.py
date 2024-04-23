# Start time: 2024-04-09 20:16:04.751592

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Summary for Input Column Data:

The input column consists of full names of individuals, each entry formatted as a single string. These names are composed of two main parts: the first name and the last name, separated by a space. The dataset includes a diverse set of names, suggesting a variety of cultural backgrounds. Each entry is unique, indicating that the data might represent a sample of individuals from a broader population. The names are presented in a standard format, with the first name followed by the last name, which is a common convention in many cultures. The dataset does not include middle names or initials, focusing solely on the primary components of a person's name.

### Summary for Output Column Data:

The output column data consists solely of first names extracted from the full names provided in the input column. Each entry in the output column corresponds directly to the first name of the individual listed in the input column. The output retains the original formatting and capitalization of the first names as they appeared in the input data. This column simplifies the information from the input by isolating a specific component of the names, demonstrating a process of data reduction and focusing on a singular aspect of the personal information provided.

### Summary of the Relationship Between Input and Output:

The relationship between the input and output columns is characterized by a process of extraction and simplification. The input column provides full names, which include both first and last names, while the output column distills this information down to only the first names. This transformation indicates a selective focus on a particular element of the data, emphasizing the importance or relevance of first names within the context of the dataset's use or analysis. The process of deriving the output from the input demonstrates a clear, systematic approach to data processing, where the initial, more complex data is streamlined into a more concise and specific subset of information. This relationship underscores the utility of data manipulation techniques in extracting meaningful insights or components from a broader dataset., and input as ['Nancy FreeHafer'] output is Nancy, input as ['Andrew Cencici'] output is Andrew, input as ['Jan Kotas'] output is Jan, input as ['Mariya Sergienko'] output is Mariya, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(full_name):
    """
    Extracts and returns the first name from a full name string.

    Parameters:
    full_name (str): A string containing a first name and a last name separated by a space.

    Returns:
    str: The first name extracted from the full name.
    """
    # Split the full name into parts assuming the first name and last name are separated by a space
    name_parts = full_name.split(' ')
    # Return the first part which is the first name
    return name_parts[0]

# Test cases
print(generated_function('Nancy FreeHafer'))  # Expected output: Nancy
print(generated_function('Andrew Cencici'))  # Expected output: Andrew
print(generated_function('Jan Kotas'))  # Expected output: Jan
print(generated_function('Mariya Sergienko'))  # Expected output: Mariya
print(generated_function("Nancy FreeHafer"))  ## Output: Nancy
print(generated_function("Andrew Cencici"))  ## Output: Andrew
print(generated_function("Jan Kotas"))  ## Output: Jan
print(generated_function("Mariya Sergienko"))  ## Output: Mariya

# End time: 2024-04-09 20:16:10.998660
# Elapsed time in seconds: 6.246934748000058


# APPEND TEST SCRIPTS...
print(generated_function("Nancy FreeHafer"))  ## Output: Nancy
print(generated_function("Andrew Cencici"))  ## Output: Andrew
print(generated_function("Jan Kotas"))  ## Output: Jan
print(generated_function("Mariya Sergienko"))  ## Output: Mariya


print(generated_function("Emma Reynolds"))  ### Output: Emma
print(generated_function("Jackson Turner"))  ### Output: Jackson
print(generated_function("Olivia Parker"))  ### Output: Olivia
print(generated_function("Lily Anderson"))  ### Output: Lily
print(generated_function("Grace Harrison"))  ### Output: Grace
print(generated_function("Benjamin Hayes"))  ### Output: Benjamin
print(generated_function("Mason Thompson"))  ### Output: Mason
print(generated_function("Caleb Mitchell"))  ### Output: Caleb
print(generated_function("Wyatt Davis"))  ### Output: Wyatt

# TEST SCRIPTS APPENDED!

