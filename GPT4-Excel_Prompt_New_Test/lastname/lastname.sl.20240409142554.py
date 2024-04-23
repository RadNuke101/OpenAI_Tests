# Start time: 2024-04-09 15:35:17.513424

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Summary of Input Column Data

The input data consists of full names of individuals, each entry comprising a first name and a last name. These names appear to be of diverse origins, indicating a variety of cultural backgrounds. The structure of each entry is consistent, with the first name followed by the last name, and both components are separated by a space. The names provided are unique in the dataset, with no repetitions of the same full name. The dataset includes both male and female first names, suggesting a gender diversity among the individuals listed. The names are presented in a standard capitalization format, where the first letter of each name is capitalized, and the rest are in lower case, adhering to common conventions in English naming practices.

### Summary of Output Column Data

The output data consists solely of the last names extracted from the full names provided in the input data. These last names are diverse, reflecting the variety of cultural backgrounds suggested by the full names. The output retains the capitalization format observed in the input data, with the first letter of each last name capitalized. The dataset of last names is unique, with no repetitions, mirroring the uniqueness of the full names in the input data. This output column simplifies the information from the input by focusing exclusively on the last names, removing the first names from consideration.

### Relationship Between Input and Output

The relationship between the input and output data is a direct extraction process, where the output is a subset of the input. Specifically, the output consists of the last names from the full names provided in the input, effectively isolating one component of the data for focused analysis or use. This process of extraction suggests an interest in the familial or cultural lineage represented by the last names, possibly for purposes where the individual's first name is deemed less relevant. The consistent structure of the input data facilitates this extraction, as the separation of first and last names by a space allows for a straightforward identification and isolation of the last names. This relationship underscores a methodological approach to data processing, where a larger set of personal information is distilled to a specific element of interest, in this case, the last names, for further use or analysis., and input as ['Nancy FreeHafer'] output is FreeHafer, input as ['Andrew Cencici'] output is Cencici, input as ['Jan Kotas'] output is Kotas, input as ['Mariya Sergienko'] output is Sergienko, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(full_name):
    """
    Extracts and returns the last name from a given full name.
    
    Parameters:
    - full_name (str): A string containing a first name and a last name separated by a space.
    
    Returns:
    - str: The last name extracted from the full name.
    """
    # Split the full name into first name and last name based on the space separator
    name_parts = full_name.split(' ')
    # Return the last name, which is the second part of the split full name
    return name_parts[1]

# Test cases
print(generated_function('Nancy FreeHafer'))  # Expected output: FreeHafer
print(generated_function('Andrew Cencici'))  # Expected output: Cencici
print(generated_function('Jan Kotas'))  # Expected output: Kotas
print(generated_function('Mariya Sergienko'))  # Expected output: Sergienko
print(generated_function("Nancy FreeHafer"))  ## Output: FreeHafer
print(generated_function("Andrew Cencici"))  ## Output: Cencici
print(generated_function("Jan Kotas"))  ## Output: Kotas
print(generated_function("Mariya Sergienko"))  ## Output: Sergienko

# End time: 2024-04-09 15:35:26.617505
# Elapsed time in seconds: 9.103905527999814


# APPEND TEST SCRIPTS...
print(generated_function("Nancy FreeHafer"))  ## Output: FreeHafer
print(generated_function("Andrew Cencici"))  ## Output: Cencici
print(generated_function("Jan Kotas"))  ## Output: Kotas
print(generated_function("Mariya Sergienko"))  ## Output: Sergienko


print(generated_function("Benjamin Hayes"))  ### Output: Hayes
print(generated_function("Liam Carter"))  ### Output: Carter
print(generated_function("Mason Thompson"))  ### Output: Thompson
print(generated_function("Sophia Coleman"))  ### Output: Coleman
print(generated_function("Ava Bennett"))  ### Output: Bennett
print(generated_function("Chloe Adams"))  ### Output: Adams
print(generated_function("Owen Morgan"))  ### Output: Morgan
print(generated_function("Wyatt Davis"))  ### Output: Davis
print(generated_function("Samuel Wright"))  ### Output: Wright
print(generated_function("Gabriel Hayes"))  ### Output: Hayes
print(generated_function("Grace Harrison"))  ### Output: Harrison
print(generated_function("Olivia Parker"))  ### Output: Parker
print(generated_function("Madison Foster"))  ### Output: Foster
print(generated_function("Nolan Cooper"))  ### Output: Cooper
print(generated_function("Caleb Johnson"))  ### Output: Johnson
print(generated_function("Lily Anderson"))  ### Output: Anderson
print(generated_function("Emma Reynolds"))  ### Output: Reynolds
print(generated_function("Caleb Mitchell"))  ### Output: Mitchell
print(generated_function("Scarlett Walker"))  ### Output: Walker
print(generated_function("Elijah Foster"))  ### Output: Foster
print(generated_function("Abigail Cooper"))  ### Output: Cooper
print(generated_function("Zoey Turner"))  ### Output: Turner
print(generated_function("Logan Smith"))  ### Output: Smith
print(generated_function("Isabella Brooks"))  ### Output: Brooks
print(generated_function("Hannah Martin"))  ### Output: Martin
print(generated_function("Aiden Clark"))  ### Output: Clark
print(generated_function("Jackson Turner"))  ### Output: Turner
print(generated_function("Carter Edwards"))  ### Output: Edwards
print(generated_function("Harper Taylor"))  ### Output: Taylor
print(generated_function("Amelia Nelson"))  ### Output: Nelson

# TEST SCRIPTS APPENDED!

