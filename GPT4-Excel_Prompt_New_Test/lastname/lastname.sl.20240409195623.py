# Start time: 2024-04-09 20:57:10.795835

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input column consists of full names of individuals, each presented in a single string format. These names follow a common pattern where the first part represents the first name of the individual, and the second part represents the last name. The names are of diverse origins, indicating a variety of cultural backgrounds. Each entry is unique, with no repetitions of the same name, suggesting a dataset that includes a wide range of individuals. The names are presented in a standard Western naming convention, where the given name precedes the surname.

### Output Column Summary:

The output column contains the last names extracted from the full names provided in the input column. These last names serve as identifiers or unique tags for each individual, separated from their first names. The extraction process appears to be consistent, with each output accurately representing the second part of the full name from the input. This column simplifies the data by focusing solely on the surname component, which could be used for sorting, indexing, or categorizing the individuals based on their family names.

### Relationship Between Input and Output:

The relationship between the input and output columns is a direct extraction process where the output is derived by isolating the last name from the full name provided in the input. This process simplifies the data by removing the first names, thus focusing on the surnames for whatever purpose deemed necessary, such as creating a more streamlined database or facilitating certain types of analyses that require only the last names. The transformation from input to output demonstrates a filtering or reduction operation, where the more complex data (full names) is distilled into a simpler form (surnames), making it easier to manage or analyze the data based on last names alone. This relationship underscores the utility of data processing techniques in organizing and simplifying information for various applications., and input as ['Nancy FreeHafer'] output is FreeHafer, input as ['Andrew Cencici'] output is Cencici, input as ['Jan Kotas'] output is Kotas, input as ['Mariya Sergienko'] output is Sergienko, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(full_name):
    """
    Extracts and returns the last name from a given full name.
    
    Parameters:
    full_name (str): A string containing the full name of an individual.
    
    Returns:
    str: The last name extracted from the full name.
    """
    # Split the full name into parts assuming the first part is the first name and the second part is the last name
    parts = full_name.split()
    # Return the last part which is assumed to be the last name
    return parts[-1]

# Test cases
print(generated_function('Nancy FreeHafer'))  # Expected output: FreeHafer
print(generated_function('Andrew Cencici'))  # Expected output: Cencici
print(generated_function('Jan Kotas'))  # Expected output: Kotas
print(generated_function('Mariya Sergienko'))  # Expected output: Sergienko
print(generated_function("Nancy FreeHafer"))  ## Output: FreeHafer
print(generated_function("Andrew Cencici"))  ## Output: Cencici
print(generated_function("Jan Kotas"))  ## Output: Kotas
print(generated_function("Mariya Sergienko"))  ## Output: Sergienko

# End time: 2024-04-09 20:57:19.687319
# Elapsed time in seconds: 8.891220221001277


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

